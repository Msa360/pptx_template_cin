from word2pptx import transform
import time

start = time.time()

transform("tests/ludification.docx", "tests/lud.pdf", "01-01-2023", 35, 11)

end = time.time()
print(f"transform executed in {end - start:.2f}s")