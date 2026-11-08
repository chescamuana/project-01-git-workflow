def show_status():
    print("Automation Service")
    print("Status: Running")


def health_check():
    return "healthy"


if __name__ == "__main__":
    show_status()
    print(f"Health: {health_check()}")