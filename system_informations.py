import platform
def system_informations():
    print("="*20, "SystemInformation", "="*20)
    unname = platform.uname()
    print(f"System: {unname.system}")
    print(f"Node Name: {unname.node}")
    print(f"Release:{unname.release}")
    print(f"Version: {unname.version}")
    print(f"Machine: {unname.machine}")
    print(f"Processor: {unname.processor}")


if __name__ == "__main__":
    system_informations()