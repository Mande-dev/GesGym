from organizations.models import SensitiveActivityLog


def log_sensitive_action(request, action, target_type="", target_label="", metadata=None, gym=None):
    organization = getattr(request, "organization", None)
    if not organization:
        return None

    return SensitiveActivityLog.objects.create(
        organization=organization,
        gym=gym or getattr(request, "gym", None),
        actor=request.user if getattr(request, "user", None) and request.user.is_authenticated else None,
        action=action,
        target_type=target_type,
        target_label=target_label,
        metadata={
            "ip": request.META.get("REMOTE_ADDR", ""),
            "path": request.path,
            **(metadata or {}),
        },
    )
