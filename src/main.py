import uvicorn

from src.utils.const import DEBUG_FLAG, PORT


def main() -> None:
    uvicorn.run("src.server:app", host="0.0.0.0", port=PORT, reload=DEBUG_FLAG)


if __name__ == '__main__':
    main()
