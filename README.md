# Django Laboratory Management System (CRUD with ORM)

A Django-based web application for managing laboratories, directors, and products. This project focuses on Django ORM (Object-Relational Mapping) and CRUD operations, created as part of a practical exercise.

## Features

- **Laboratory Management**: Create, read, update, and delete laboratory records.
- **Director Management**: Assign and manage directors associated with laboratories.
- **Product Management**: Track products linked to laboratories, including details like price and stock.
- **Admin Integration**: Use Django's admin panel to manage data.
- **ORM Practice**: Demonstrates Django ORM usage for database interactions.
- **Tests Included**: Unit tests for models and views.

## Technologies Used

- **Django**: High-level Python web framework.
- **PostgreSQL**: Default database 
- **Bootstrap**: Frontend styling for templates.
- **Django ORM**: For database operations and model relationships.

## Models

1. **Laboratorio**:
   - Fields: `id`, `nombre`, `ciudad`, `pais`.
2. **DirectorGeneral**:
   - Fields: `id`, `nombre`, `laboratorio` (One-to-One relationship with `Laboratorio`).
3. **Producto**:
   - Fields: `id`, `nombre`, `laboratorio` (ForeignKey to `Laboratorio`), `f_fabricacion`, `p_costo`, `p_venta`.

## Installation
1. Clone the repository:
2. Install dependencies. (requirements.txt)
3. Run migrations
4. Run the server

## Usage
-View Labs: Navigate to /laboratorio/ to see a list of labs.
-Add/Edit Labs: Use the "Crear Laboratorio" or "Editar" buttons.
-Delete Labs: Click "Eliminar" next to a lab (requires confirmation).
