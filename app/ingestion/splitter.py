from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, documents):

        chunks = self.text_splitter.split_documents(documents)

        print(f"Created {len(chunks)} chunks.")

        return chunks