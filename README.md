# nrcm

An application in the karun99 portfolio.

## Quick start

```bash
python3 -m http.server 8080
python3 mcp-server/mcp_server.py
```

## MCP server
## MCP server

This application ships a dependency-free [Model Context Protocol](https://modelcontextprotocol.io)
server (`mcp-server/mcp_server.py`) exposing its core operations to agentic clients.
It speaks JSON-RPC 2.0 over stdio and adds no runtime dependencies.

Add the repository's [`.mcp.json`](.mcp.json) to your MCP client, or run:

```bash
python3 mcp-server/mcp_server.py
```

Protocol smoke tests:

```bash
python3 -m unittest discover -s tests -p "test_mcp_server.py" -v
```

See [docs/MCP.md](docs/MCP.md) and [mcp-server/README.md](mcp-server/README.md).


## Testing

```bash
python3 -m unittest discover -s tests -p "test_mcp_server.py" -v
```

## License

MIT (see [LICENSE](LICENSE)) unless noted otherwise.


## Quick start & testing

```bash
# run the nrcm
python3 -m http.server 8080
python3 mcp-server/mcp_server.py

# verify the MCP server speaks the protocol
python3 -m unittest discover -s tests -p "test_mcp_server.py" -v
```

See [docs/MCP.md](docs/MCP.md) for the exposed tools. All files were generated
(and the application hardened) by the TRL rollout in `mcp-server/`.
