import unittest

from cvgenius.data.templates.template_registry import (
    TemplateDefinition,
    get_available_templates,
    get_template,
)


class TemplateRegistryTests(unittest.TestCase):
    def test_registry_contains_builtin_templates(self):
        templates = get_available_templates()

        self.assertTrue(any(item.name == "classic" for item in templates))
        self.assertTrue(any(item.name == "modern" for item in templates))

    def test_get_template_returns_definition(self):
        template = get_template("classic")

        self.assertIsInstance(template, TemplateDefinition)
        self.assertEqual(template.name, "classic")
        self.assertIn("classic", template.label.lower())


if __name__ == "__main__":
    unittest.main()
