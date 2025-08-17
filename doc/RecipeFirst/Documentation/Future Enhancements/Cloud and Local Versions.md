# Summary

RecipeFirst should have both cloud and locally hosted options.

## Timeline

Late in the development cycle. Near or even after production release

## Considerations

Things to keep in mind, potential issues, or predictable roadblocks

### Architecture Incompatible with Cloud

The sqlite/FastAPI backend is going to be largely redundant on AWS unless I want to host everything on an EC2 instance and pay way too much money for hosting.

- Will need to rewrite the FastAPI implementation using Lambda functions and API Gateway instead
- The frontend will probably transfer pretty cleanly if it's properly decoupled from the data layer.

## Features

### Cloud

- No installation required
- Comes with default data automatically
- Paid (?)

### Local

- Installation required

- Unless I architect this specifically for Windows (I won't be), then it will require Linux/WSL to install

- Comes with no data automatically; a blank slate

- Default data optional during or after installation

- Free / Paid

- Base functionality should be free.
- Future potential AI features will be premium and require a subscription