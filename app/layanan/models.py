from django.db import models
from safedelete.models import HARD_DELETE, SafeDeleteModel


class LayananPemerintahan(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE

    keperluan = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "auths.User",
        on_delete=models.CASCADE,
        related_name="layanan_pemerintahan_created",
    )
    updated_by = models.ForeignKey(
        "auths.User",
        on_delete=models.CASCADE,
        related_name="layanan_pemerintahan_updated",
    )

    class Meta:
        db_table = "layanan_pemerintahan"


class LayananUmum(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE

    keperluan = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "auths.User",
        on_delete=models.CASCADE,
        related_name="layanan_umum_created",
    )
    updated_by = models.ForeignKey(
        "auths.User",
        on_delete=models.CASCADE,
        related_name="layanan_umum_updated",
    )

    class Meta:
        db_table = "layanan_umum"
