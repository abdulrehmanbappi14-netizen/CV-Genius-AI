from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TemplateDefinition:
    name: str
    label: str
    description: str


_TEMPLATE_REGISTRY = {
    "classic": TemplateDefinition(
        name="classic",
        label="Classic Resume",
        description="A traditional and clean resume template.",
    ),
    "modern": TemplateDefinition(
        name="modern",
        label="Modern Resume",
        description="A more contemporary layout-friendly template.",
    ),
}


def get_available_templates() -> list[TemplateDefinition]:
    return list(_TEMPLATE_REGISTRY.values())


def get_template(name: str) -> TemplateDefinition:
    return _TEMPLATE_REGISTRY[name]
