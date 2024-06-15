from enum import Enum

from .domain.document import Document
from .domain.template import DocumentTemplate, SectionTemplate

ADR_NYGAARD_TEMPLATE = DocumentTemplate(
    sections=[
        SectionTemplate(
            title="Decision record template by Michael Nygard",
            size=1,
        ),
        SectionTemplate(
            title="Title",
            size=1,
        ),
        SectionTemplate(
            title="Status",
            size=2,
        ),
        SectionTemplate(
            title="Context",
            size=2,
        ),
        SectionTemplate(
            title="Decision",
            size=2,
        ),
        SectionTemplate(
            title="Consequences",
            size=2,
        ),
    ],
)

ADR_EDGEX_TEMPLATE = DocumentTemplate(
    sections=[
        SectionTemplate(
            title="Architecture Decision Record (ADR) template"
            " <!-- Replace with ADR title -->",
            size=1,
        ),
        SectionTemplate(
            title="Submitters",
            size=3,
        ),
        SectionTemplate(
            title="Change Log",
            size=2,
        ),
        SectionTemplate(
            title="Referenced Use Case(s)",
            size=2,
        ),
        SectionTemplate(
            title="Context",
            size=2,
        ),
        SectionTemplate(
            title="Proposed Design",
            size=2,
        ),
        SectionTemplate(
            title="Considerations",
            size=2,
        ),
        SectionTemplate(
            title="Decision",
            size=2,
        ),
        SectionTemplate(
            title="Other Related ADRs",
            size=2,
        ),
        SectionTemplate(
            title="References",
            size=2,
        ),
    ],
)


class Template(Enum):
    ADR_NYGAARD = ADR_NYGAARD_TEMPLATE
    ADR_EDGEX = ADR_EDGEX_TEMPLATE

    def matches(self, document: Document) -> bool:
        return self.value.matches(document)
