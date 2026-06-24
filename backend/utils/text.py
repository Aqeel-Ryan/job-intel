"""Text utilities: cleaning and slug generation."""


def slugify(name: str) -> str:
    """Convert a company name into a URL-safe slug.

    Args:
        name: The raw company name.

    Returns:
        A lowercase, hyphen-separated slug (e.g. "Acme Corp" -> "acme-corp").
    """
    # TODO: lowercase, strip, collapse non-alphanumerics into single hyphens.
    raise NotImplementedError


def clean_text(raw: str) -> str:
    """Normalise scraped text: collapse whitespace, strip boilerplate.

    Args:
        raw: Raw scraped text (often containing HTML artefacts and runs of
            whitespace).

    Returns:
        Cleaned, single-spaced text suitable for LLM input.
    """
    # TODO: unescape HTML entities, strip tags, collapse whitespace.
    raise NotImplementedError
