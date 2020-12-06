import Services.fast_api as fa
import uvicorn


def main():
    app = fa.app
    uvicorn.run(app, host="0.0.0.0", port=8001)


if __name__ == '__main__':
    main()
