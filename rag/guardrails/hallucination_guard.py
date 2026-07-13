class HallucinationGuard:
    """Validate generated responses."""

    DEFAULT_RESPONSE = (
        "I don't know based on the provided documents."
    )

    @staticmethod
    def validate(response):
        if not response:
            return HallucinationGuard.DEFAULT_RESPONSE

        answer = response.strip()

        if not answer:
            return HallucinationGuard.DEFAULT_RESPONSE

        return answer