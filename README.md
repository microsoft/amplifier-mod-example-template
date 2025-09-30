# amplifier-mod-example-template

This repository is a **living template** for building Amplifier modules. It demonstrates how to:

- Ship a tool and/or model provider that registers with the Amplifier kernel
- Structure a module as an isolated "brick" with tests and docs
- Load the module via manifest entries using either a local path or git reference

The template is intentionally simple so it can be cloned and customized. Replace the example tool
with your own logic, update the manifest snippet, and you're ready to go.

## Getting Started

```bash
uv pip install -e .[dev]
uv run pytest
```

## Manifest Snippet

```toml
[[modules]]
name = "example-template"
entrypoint = "amplifier_mod_example_template:register"
path = "../amplifier-mod-example-template/src"
config = { message = "Hello from template" }
```

If you publish the module to a git repo, you can swap `path` for `git = "https://..."` and optionally
add `ref = "v1.0.0"`.

## Customization Checklist

1. Rename the module directory and update `entrypoint`
2. Adjust `register()` to expose your tools/providers
3. Add targeted tests under `tests/`
4. Update this README with usage notes specific to your module
5. Tag a release or provide clear instructions for referencing via manifest

By keeping this template in sync with the core repo we ensure new modules share a consistent shape
and remain easy for humans and AI tools to understand.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

