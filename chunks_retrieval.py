from fastapi import Request
from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Any

class IngestedDoc(BaseModel):
    object: Literal["ingest.document"]
    doc_id: str = Field(examples=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"])
    doc_metadata: Optional[dict[str, Any]] = Field(
        examples=[
            {
                "page_label": "2",
                "file_name": "Sales Report Q3 2023.pdf",
            }
        ]
    )

    @staticmethod
    def curate_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
        """Remove unwanted metadata keys."""
        for key in ["doc_id", "window", "original_text"]:
            metadata.pop(key, None)
        return metadata

    @staticmethod
    def from_document(document: Document) -> "IngestedDoc":
        return IngestedDoc(
            object="ingest.document",
            doc_id=document.doc_id,
            doc_metadata=IngestedDoc.curate_metadata(document.metadata),
        )

class ContextFilter(BaseModel):
    docs_ids: Optional[List[str]] = Field(
        examples=[["c202d5e6-7b69-4869-81cc-dd574ee8ee11"]]
    )

class ChunksBody(BaseModel):
    text: str = Field(examples=["Q3 2023 sales"])
    context_filter: Optional[ContextFilter] = None
    limit: int = 10
    prev_next_chunks: int = Field(default=0, examples=[2])

class Chunk(BaseModel):
    object: Literal["context.chunk"]
    score: float = Field(examples=[0.023])
    document: IngestedDoc
    text: str = Field(examples=["Outbound sales increased 20%, driven by new leads."])
    previous_texts: Optional[List[str]] = Field(
        default=None,
        examples=[["SALES REPORT 2023", "Inbound didn't show major changes."]],
    )
    next_texts: Optional[List[str]] = Field(
        default=None,
        examples=[
            [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department",
            ]
        ],
    )

    @classmethod
    def from_node(cls: type["Chunk"], node: NodeWithScore) -> "Chunk":
        doc_id = node.node.ref_doc_id if node.node.ref_doc_id is not None else "-"
        return cls(
            object="context.chunk",
            score=node.score or 0.0,
            document=IngestedDoc(
                object="ingest.document",
                doc_id=doc_id,
                doc_metadata=node.metadata,
            ),
            text=node.get_content(),
        )

class ChunksResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: List[Chunk]

def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse:
    """Given a `text`, returns the most relevant chunks from the ingested documents.

    The returned information can be used to generate prompts that can be
    passed to `/completions` or `/chat/completions` APIs. Note: it is usually a very
    fast API, because only the Embeddings model is involved, not the LLM. The
    returned information contains the relevant chunk `text` together with the source
    `document` it is coming from. It also contains a score that can be used to
    compare different results.

    The max number of chunks to be returned is set using the `limit` param.

    Previous and next chunks (pieces of text that appear right before or after in the
    document) can be fetched by using the `prev_next_chunks` field.

    The documents being used can be filtered using the `context_filter` and passing
    the document IDs to be used. Ingested documents IDs can be found using
    `/ingest/list` endpoint. If you want all ingested documents to be used,
    remove `context_filter` altogether.
    """
    service = request.state.injector.get(ChunksService)
    # 固定文檔ID
    fixed_doc_id = "your_fixed_doc_id"
    if body.context_filter:
        body.context_filter.docs_ids = [fixed_doc_id]
    else:
        body.context_filter = ContextFilter(docs_ids=[fixed_doc_id])
    
    results = service.retrieve_relevant(
        body.text, 
        body.context_filter.docs_ids, 
        body.limit, 
        body.prev_next_chunks
    )
    return ChunksResponse(
        object="list",
        model="private-gpt",
        data=results,
    )

# 示例用法
if __name__ == "__main__":
    request_body = ChunksBody(
        text="What is apple?",
        context_filter=ContextFilter(docs_ids=["your_fixed_doc_id"])  # 替換為你的文檔ID
    )

    # 假設 request 是一個已經存在的 Request 對象
    response = chunks_retrieval(request, request_body)
    print(response)
