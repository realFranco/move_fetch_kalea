"""
API
"""
import time

from app.service.browser import Browser


b = Browser()
b.instance()
b.go_to_kalea(item_label='agua')
# Debatible
time.sleep(2.5)
b.kalea_expand_results()
# b.fetch()

b.quit()
