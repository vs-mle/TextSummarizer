import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "vs-mle"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL="vsmachinelearning@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    authot = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="small python package for summarizing text - nlp e2e",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
