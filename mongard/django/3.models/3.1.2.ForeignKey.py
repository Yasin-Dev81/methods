"""
- برای ارتباط دادن یه مادل به مادلی دیگر
- حالات مختلف فارن کی ها
    * O2O: One2One
    * M2M: Many2Many
    * M2O: Many2One

- اگر حذف شد چه اتفاقی برای مادل های وابسته اش بیوفتد
- on_delete options:
    * CASCADE
        ~ حذف شدن هردو دیتا
    * SET_NULL
        ~ بجاش خالی قرار بده
    * PROTECT
    * TESTRICT
    * SET_DEFAULT
    * SET()

# related_name: معکوس حرکت کردن در فارن کی ها
- M2M, M2O
    * <data of moder model>.>RelatedModel>_set.all()
        ~ ex: u1.post_set.all()
        ~ حروف کوچیک باشه
        ~ Post > post_set

- O2O, M2M, M2O
    * ForeignKey(..., related_name='...')

- فارن کی زدن به خود مادل
    * برای ریپلای کامنت ها بکار میاد
    * models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    * models.ForeignKey('<model-name>', on_delete=models.CASCADE, blank=True, null=True)
"""
