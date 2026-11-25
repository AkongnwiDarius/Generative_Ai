import os
from tools.Rag_tool import smart_retrieval_tool

# Ensure you have a test folder with dummy files (e.g., .txt or .pdf files)
TEST_FOLDER = "./test_docs"

def test_retrieval():
    # Make sure test folder exists
    if not os.path.exists(TEST_FOLDER):
        print(f"Please create a folder named '{TEST_FOLDER}' with test documents.")
        return

    print("Running direct tool test...")
    
    # 1. Test tool invocation directly
    query = "What is the main topic of these documents?"
    
    try:
        results = smart_retrieval_tool.invoke({
            "query": query,
            "folder_path": TEST_FOLDER,
            "k": 2
        })
        
        print(f"\n--- Retrived {len(results)} Chunk(s) ---")
        for i, doc in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(f"Content: {doc.page_content[:200]}...")  # Show first 200 chars
            print(f"Metadata: {doc.metadata}")

    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    test_retrieval()