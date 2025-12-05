import os  
import random  
import sys
import argparse
import time
  
code="""from hashlib import blake2b  
from functools import lru_cache  
from itertools import count, product  
from collections import Counter  
import sys, json, os, time  
import math, random  
import base64  
  
lc_code="CmZyb20gaGFzaGxpYiBpbXBvcnQgYmxha2UyYgpmcm9tIGZ1bmN0b29scyBpbXBvcnQgbHJ1X2NhY2hlCmZyb20gaXRlcnRvb2xzIGltcG9ydCBjb3VudCwgcHJvZHVjdApmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCmltcG9ydCBzeXMsIGpzb24sIG9zLCB0aW1lCmltcG9ydCBtYXRoLCByYW5kb20KCnN5cy5zZXRfaW50X21heF9zdHJfZGlnaXRzKCgyKiozMSktMSkKdmVyc2lvbiA9IDkKCmNsYXNzIExlQ2F0Y2h1X0VuZ2luZTogICMgTGVDYXRjaHUgTGVobkNBVEg0IEVuZ2luZQogICAgZGVmIF9faW5pdF9fKHNlbGYsIHNib3hzZWVkPSJMZWhuY3J5cHQiLCBzYm94c2VlZHhiYXNlPTEsIGVuY29kaW5nX3R5cGU9InBhY2tldCIsIGRhdGE9IiIsIHNodWZmbGVzYm94PUZhbHNlLCBzZXBlcmF0b3Jwcm92PVRydWUsIGVuY29kaW5nPUZhbHNlLCB1bmljb2Rlc3VwcG9ydD0xMTE0MTEyLCBwZXJsZW5ndGg9Mywgc3BlY2lhbF9leGNoYW5nZT1Ob25lKToKICAgICAgICBzZWxmLnNwZWNpYWxfZXhjaGFuZ2UgPSBzcGVjaWFsX2V4Y2hhbmdlCiAgICAgICAgaWYgbGVuKGRhdGEpID4gMDoKICAgICAgICAgICAgc2VsZi5fX29yZ19lbmNvZGUgPSBzZWxmLmVuY29kZQogICAgICAgICAgICBzZWxmLl9fb3JnX2RlY29kZSA9IHNlbGYuZGVjb2RlCiAgICAgICAgICAgIHNlbGYuX19vcmdfY2FjaGVkX2hhc2ggPSBzZWxmLmNhY2hlZF9oYXNoCiAgICAgICAgICAgIHNlbGYubG9hZChkYXRhKQogICAgICAgIGVsaWYgZW5jb2Rpbmc6CiAgICAgICAgICAgIHNlbGYuc2JveCA9IHt9CiAgICAgICAgICAgIHNlbGYucmVzYm94ID0ge30KICAgICAgICAgICAgaW1wb3J0IHJhbmRvbSBhcyB0ZW1wcmFuZG9tCiAgICAgICAgICAgIHRlbXByYW5kb20uc2VlZChzZWxmLnByb2Nlc3NfaGFzaChzYm94c2VlZCwgc2JveHNlZWR4YmFzZSkpCiAgICAgICAgICAgIG14biA9IDI1NiBpZiBlbmNvZGluZ190eXBlID09ICJwYWNrZXQiIGVsc2UgMjU1CiAgICAgICAgICAgIGlmIGVuY29kaW5nX3R5cGUgPT0gInNlcGVyYXRvciIgYW5kIHNlcGVyYXRvcnByb3Y6CiAgICAgICAgICAgICAgICBucyA9IHN1bShbW2J5dGVzKGNvbWJvKSBmb3IgY29tYm8gaW4gcHJvZHVjdChyYW5nZShteG4pLCByZXBlYXQ9aSsxKV0gZm9yIGkgaW4gcmFuZ2UocGVybGVuZ3RoKV0sIHN0YXJ0PVtdKQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgbnMgPSBbYnl0ZXMoY29tYm8pIGZvciBjb21ibyBpbiBwcm9kdWN0KHJhbmdlKG14biksIHJlcGVhdD1wZXJsZW5ndGgpXQogICAgICAgICAgICBpZiBzaHVmZmxlc2JveDoKICAgICAgICAgICAgICAgIHRlbXByYW5kb20uc2h1ZmZsZShucykKICAgICAgICAgICAgZm9yIHVuaW4sIG4gaW4gZW51bWVyYXRlKG5zWzp1bmljb2Rlc3VwcG9ydF0pOiAgIyBEZWZpbmUgc2JveCBjaGFyYWN0ZXJzIGFuZCB0aGVpciBlcXVpdmFsZW50cwogICAgICAgICAgICAgICAgc2VsZi5zYm94W2Nocih1bmluKV0gPSBuCiAgICAgICAgICAgICAgICBzZWxmLnJlc2JveFtuXSA9IGNocih1bmluKQogICAgICAgICAgICBzZWxmLl9fb3JnX2VuY29kZSA9IHNlbGYuZW5jb2RlCiAgICAgICAgICAgIHNlbGYuX19vcmdfZGVjb2RlID0gc2VsZi5kZWNvZGUKICAgICAgICAgICAgaWYgZW5jb2RpbmdfdHlwZSA9PSAic2VwZXJhdG9yIjoKICAgICAgICAgICAgICAgIHNlbGYuZW5jb2RlID0gc2VsZi5fX3NlcF9lbmNvZGUKICAgICAgICAgICAgICAgIHNlbGYuZGVjb2RlID0gc2VsZi5fX3NlcF9kZWNvZGUKICAgICAgICAgICAgc2VsZi5lbmNvZGluZ190eXBlID0gZW5jb2RpbmdfdHlwZQogICAgICAgICAgICBzZWxmLnBlcmxlbmd0aCA9IHBlcmxlbmd0aAogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHNlbGYuZW5jb2RpbmdfdHlwZSA9IGVuY29kaW5nX3R5cGUKICAgICAgICAgICAgc2VsZi5fX29yZ19lbmNvZGUgPSBzZWxmLmVuY29kZQogICAgICAgICAgICBzZWxmLl9fb3JnX2RlY29kZSA9IHNlbGYuZGVjb2RlCiAgICAgICAgICAgIHNlbGYuc2JveCA9IHt9CiAgICAgICAgICAgIHNlbGYucmVzYm94ID0ge30KICAgICAgICBzZWxmLmVuY29kaW5nID0gZW5jb2RpbmcKICAgICAgICBzZWxmLnVuaWNvZGVzdXBwb3J0ID0gdW5pY29kZXN1cHBvcnQKICAgICAgICBzZWxmLnNodWZmbGVzYm94ID0gc2h1ZmZsZXNib3gKICAgICAgICBzZWxmLl9fb3JnX2NhY2hlZF9oYXNoID0gc2VsZi5jYWNoZWRfaGFzaAogICAgICAgIGlmIHNlbGYuc3BlY2lhbF9leGNoYW5nZToKICAgICAgICAgICAgc2VsZi5jYWNoZWRfaGFzaCA9IHNlbGYuX19zcGVjaWFsX2V4Y2hhbmdlZF9jYWNoZWRfaGFzaAoKICAgIGRlZiBlbmNvZGUoc2VsZiwgc3RyaW5nKTogICMgRXJyb3ItZnJlZSBlbmNvZGluZyBvZiBzdHJpbmcgZGF0YSAoYWxsIGNoYXJhY3RlcnMgc3VwcG9ydGVkKQogICAgICAgIHJldHVybiBiIiIuam9pbihbc2VsZi5zYm94W2ldIGZvciBpIGluIHN0cmluZ10pCgogICAgZGVmIF9fc2VwX2VuY29kZShzZWxmLCBzdHJpbmcpOiAgIyBFcnJvci1mcmVlIGVuY29kaW5nIG9mIHN0cmluZyBkYXRhIChhbGwgY2hhcmFjdGVycyBzdXBwb3J0ZWQpICh3aXRoIHNlcGVyYXRvcikKICAgICAgICByZXR1cm4gYnl0ZXMoWzI1NV0pLmpvaW4oW3NlbGYuc2JveFtpXSBmb3IgaSBpbiBzdHJpbmddKQoKICAgIGRlZiBkZWNvZGUoc2VsZiwgYnl0ZXN0ZXh0KTogICMgRGVjb2RlIHRoZSBieXRlIGRhdGEKICAgICAgICByZXR1cm4gIiIuam9pbihbc2VsZi5yZXNib3hbYnl0ZXN0ZXh0W2k6aStzZWxmLnBlcmxlbmd0aF1dIGZvciBpIGluIHJhbmdlKDAsIGxlbihieXRlc3RleHQpLCBzZWxmLnBlcmxlbmd0aCldKQoKICAgIGRlZiBfX3NlcF9kZWNvZGUoc2VsZiwgYnl0ZXN0ZXh0KTogICMgRGVjb2RlIHRoZSBieXRlIGRhdGEgKHdpdGggc2VwZXJhdG9yKQogICAgICAgIHJldHVybiAiIi5qb2luKFtzZWxmLnJlc2JveFtpXSBmb3IgaSBpbiBieXRlc3RleHQuc3BsaXQoYnl0ZXMoWzI1NV0pKV0pCgogICAgQGxydV9jYWNoZShtYXhzaXplPTEyOCkKICAgIGRlZiBjYWNoZWRfaGFzaChzZWxmLCBjb21iayk6CiAgICAgICAgcmV0dXJuIGJsYWtlMmIoY29tYmsuZW5jb2RlKCksIGRpZ2VzdF9zaXplPTMyKS5oZXhkaWdlc3QoKQoKICAgIEBscnVfY2FjaGUobWF4c2l6ZT0xMjgpCiAgICBkZWYgX19zcGVjaWFsX2V4Y2hhbmdlZF9jYWNoZWRfaGFzaChzZWxmLCBjb21iayk6CiAgICAgICAgcmV0dXJuIGJsYWtlMmIoKGNvbWJrICsgc2VsZi5zcGVjaWFsX2V4Y2hhbmdlKS5lbmNvZGUoKSwgZGlnZXN0X3NpemU9MzIpLmhleGRpZ2VzdCgpCgogICAgQGxydV9jYWNoZShtYXhzaXplPTY0KQogICAgZGVmIHByb2Nlc3NfaGFzaChzZWxmLCBrZXksIHhiYXNlPTEpOgogICAgICAgIGtleSA9IG9rZXkgPSBzdHIoa2V5KQogICAgICAgIGhhc2hzID0gW2tleTo9c2VsZi5jYWNoZWRfaGFzaCgoa2V5ICsgb2tleSkpIGZvciBfIGluIHJhbmdlKHhiYXNlKV0KICAgICAgICByZXR1cm4gaW50KCIiLmpvaW4oaGFzaHMpLCAxNikKCiAgICBkZWYgaGFzaF9zdHJlYW0oc2VsZiwga2V5LCB4YmFzZT0xLCBpbnRlcnZhbD0xKToKICAgICAgICBrZXkgPSBva2V5ID0gdGtleSA9IHN0cihrZXkpCiAgICAgICAgaWYgaW50ZXJ2YWwgPT0gMToKICAgICAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgICAgIHRrZXkgPSBzdHIoa2V5KQogICAgICAgICAgICAgICAgeWllbGQgaW50KCIiLmpvaW4oW2tleTo9c2VsZi5jYWNoZWRfaGFzaCgoa2V5ICsgb2tleSArIHRrZXkpKSBmb3IgXyBpbiByYW5nZSh4YmFzZSldKSwgMTYpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgZm9yIGkgaW4gY291bnQoKToKICAgICAgICAgICAgICAgIGlmIGkgJSBpbnRlcnZhbCA9PSAwOgogICAgICAgICAgICAgICAgICAgIHRrZXkgPSBzdHIoa2V5KQogICAgICAgICAgICAgICAgICAgIGVrZXkgPSBpbnQoIiIuam9pbihba2V5Oj1zZWxmLmNhY2hlZF9oYXNoKChrZXkgKyBva2V5ICsgdGtleSkpIGZvciBfIGluIHJhbmdlKHhiYXNlKV0pLCAxNikKICAgICAgICAgICAgICAgIHlpZWxkIGVrZXkKCiAgICBkZWYgaGFzaF9zdHJlYW1zKHNlbGYsIGtleXMsIHhiYXNlPTEsIGludGVydmFsPTEpOgogICAgICAgIG9rZXkgPSAiIi5qb2luKFtzdHIoa2V5KSBmb3Iga2V5IGluIGtleXNdKQogICAgICAgIGtleWdlbnMgPSBbc2VsZi5oYXNoX3N0cmVhbShzdHIoa2V5KSArIG9rZXksIHhiYXNlLCBpbnRlcnZhbCkgZm9yIGtleSBpbiBrZXlzXSArIFtzZWxmLmhhc2hfc3RyZWFtKG9rZXksIHhiYXNlKV0KICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICB5aWVsZCBzdW0oW25leHQoa2V5KSBmb3Iga2V5IGluIGtleWdlbnNdKQoKICAgIGRlZiBlbmNyeXB0KHNlbGYsIGJ5dGVzdGFyZ2V0LCBrZXksIHhiYXNlPTEsIGludGVydmFsPTEpOgogICAgICAgIGtleWdlbiA9IHNlbGYuaGFzaF9zdHJlYW0oa2V5LCB4YmFzZSwgaW50ZXJ2YWwpCiAgICAgICAgcmV0dXJuIGJ5dGVzKFsoYnl0ZXN0YXJnZXRbaV0gKyBuZXh0KGtleWdlbikpICUgMjU2IGZvciBpIGluIHJhbmdlKGxlbihieXRlc3RhcmdldCkpXSkKCiAgICBkZWYgZGVjcnlwdChzZWxmLCBieXRlc3RhcmdldCwga2V5LCB4YmFzZT0xLCBpbnRlcnZhbD0xKToKICAgICAgICBrZXlnZW4gPSBzZWxmLmhhc2hfc3RyZWFtKGtleSwgeGJhc2UsIGludGVydmFsKQogICAgICAgIHJldHVybiBieXRlcyhbKGJ5dGVzdGFyZ2V0W2ldIC0gbmV4dChrZXlnZW4pKSAlIDI1NiBmb3IgaSBpbiByYW5nZShsZW4oYnl0ZXN0YXJnZXQpKV0pCgogICAgZGVmIGVuY3J5cHRfd2l0aF9pdihzZWxmLCBieXRlc3RhcmdldCwga2V5LCB4YmFzZT0xLCBpbnRlcnZhbD0xLCBpdmxlbmd0aD0yNTYsIGl2eGJhc2U9MSwgaXZpbnRlcnZhbD0xKTogICMgcmVjb21tZW5kZWQKICAgICAgICByZXR1cm4gc2VsZi5lbmNyeXB0KHNlbGYuYWRkaXYoYnl0ZXN0YXJnZXQsIGl2bGVuZ3RoLCBpdnhiYXNlLCBpdmludGVydmFsKSwga2V5LCB4YmFzZSwgaW50ZXJ2YWwpCgogICAgZGVmIGRlY3J5cHRfd2l0aF9pdihzZWxmLCBieXRlc3RhcmdldCwga2V5LCB4YmFzZT0xLCBpbnRlcnZhbD0xLCBpdmxlbmd0aD0yNTYsIGl2eGJhc2U9MSwgaXZpbnRlcnZhbD0xKTogICMgcmVjb21tZW5kZWQKICAgICAgICByZXR1cm4gc2VsZi5kZWxpdihzZWxmLmRlY3J5cHQoYnl0ZXN0YXJnZXQsIGtleSwgeGJhc2UsIGludGVydmFsKSwgaXZsZW5ndGgsIGl2eGJhc2UsIGl2aW50ZXJ2YWwpCgogICAgZGVmIGVuY3J5cHRzKHNlbGYsIGJ5dGVzdGFyZ2V0LCBrZXlzLCB4YmFzZT0xLCBpbnRlcnZhbD0xKToKICAgICAgICBrZXlnZW4gPSBzZWxmLmhhc2hfc3RyZWFtcyhrZXlzLCB4YmFzZSwgaW50ZXJ2YWwpCiAgICAgICAgcmV0dXJuIGJ5dGVzKFsoYnl0ZXN0YXJnZXRbaV0gKyBuZXh0KGtleWdlbikpICUgMjU2IGZvciBpIGluIHJhbmdlKGxlbihieXRlc3RhcmdldCkpXSkKCiAgICBkZWYgZGVjcnlwdHMoc2VsZiwgYnl0ZXN0YXJnZXQsIGtleXMsIHhiYXNlPTEsIGludGVydmFsPTEpOgogICAgICAgIGtleWdlbiA9IHNlbGYuaGFzaF9zdHJlYW1zKGtleXMsIHhiYXNlLCBpbnRlcnZhbCkKICAgICAgICByZXR1cm4gYnl0ZXMoWyhieXRlc3RhcmdldFtpXSAtIG5leHQoa2V5Z2VuKSkgJSAyNTYgZm9yIGkgaW4gcmFuZ2UobGVuKGJ5dGVzdGFyZ2V0KSldKQoKICAgIGRlZiBlbmNvZGVfZGlyZWN0KHNlbGYsIHRleHQpOgogICAgICAgIHJldHVybiBieXRlcyhbb3JkKGkpIGZvciBpIGluIHRleHRdKQoKICAgIGRlZiBkZWNvZGVfZGlyZWN0KHNlbGYsIGJ5dGVzdGV4dCk6CiAgICAgICAgcmV0dXJuICIiLmpvaW4oW2NocihieXRlc3RleHRbaV0pIGZvciBpIGluIHJhbmdlKGxlbihieXRlc3RleHQpKV0pCgogICAgZGVmIGFkZF90YWN0YWcoc2VsZiwgYnl0ZXN0ZXh0LCBleHQ9YiJNVEciLCBleHR4YmFzZT0xLCB4YmFzZT0xLCBpbnRlcnZhbD0xLCBpdmxlbmd0aD0yNTYsIGl2eGJhc2U9MSwgaXZpbnRlcnZhbD0xKToKICAgICAgICBleHQyID0gc3RyKHNlbGYucHJvY2Vzc19oYXNoKGV4dCwgZXh0eGJhc2UpKS5lbmNvZGUoKQogICAgICAgIHJldHVybiBzZWxmLmVuY3J5cHRfd2l0aF9pdihleHQyICsgYnl0ZXN0ZXh0ICsgZXh0MiwgZXh0MiwgeGJhc2UsIGludGVydmFsLCBpdmxlbmd0aCwgaXZ4YmFzZSwgaXZpbnRlcnZhbCkKCiAgICBkZWYgY2hlY2tfdGFjdGFnKHNlbGYsIGJ5dGVzdGV4dCwgZXh0PWIiTVRHIiwgZXh0eGJhc2U9MSwgeGJhc2U9MSwgaW50ZXJ2YWw9MSwgaXZsZW5ndGg9MjU2LCBpdnhiYXNlPTEsIGl2aW50ZXJ2YWw9MSk6CiAgICAgICAgZXh0MiA9IHN0cihzZWxmLnByb2Nlc3NfaGFzaChleHQsIGV4dHhiYXNlKSkuZW5jb2RlKCkKICAgICAgICBieXRlc3RleHQgPSBzZWxmLmRlY3J5cHRfd2l0aF9pdihieXRlc3RleHQsIGV4dDIsIHhiYXNlLCBpbnRlcnZhbCwgaXZsZW5ndGgsIGl2eGJhc2UsIGl2aW50ZXJ2YWwpCiAgICAgICAgaWYgYnl0ZXN0ZXh0WzpsZW4oZXh0MildID09IGV4dDIgYW5kIGJ5dGVzdGV4dFstbGVuKGV4dDIpOl0gPT0gZXh0MjoKICAgICAgICAgICAgcmV0dXJuIGJ5dGVzdGV4dFtsZW4oZXh0Mik6XVs6LWxlbihleHQyKV0KICAgICAgICBlbHNlOgogICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJDaGVjayBmYWlsZWQ6IFRBQyB0YWcgbm90IGZvdW5kIG9yIGludmFsaWQuIikKCiAgICBkZWYgc2F2ZShzZWxmKToKICAgICAgICBzYm94ID0ge30KICAgICAgICBmb3IgaTEsIGkyIGluIHNlbGYuc2JveC5pdGVtcygpOgogICAgICAgICAgICBibCA9ICIsIi5qb2luKFtzdHIoaTJbaV0pIGZvciBpIGluIHJhbmdlKDMpXSkgICMgbGlzdGVkIGJ5dGVzCiAgICAgICAgICAgIHNib3hbaTFdID0gYmwKICAgICAgICByZXR1cm4ganNvbi5kdW1wcyh7InNib3giOiBzYm94LCAiZW5jb2RpbmdfdHlwZSI6IHNlbGYuZW5jb2RpbmdfdHlwZSwgInNwZWNpYWxfZXhjaGFuZ2UiOiBzZWxmLnNwZWNpYWxfZXhjaGFuZ2UsICJwZXJsZW5ndGgiOiBzZWxmLnBlcmxlbmd0aCwgInZlcnNpb24iOiA5fSkKCiAgICBkZWYgbG9hZChzZWxmLCBkYXRhKToKICAgICAgICBkYXRhID0ganNvbi5sb2FkcyhkYXRhKQogICAgICAgIGlmIGRhdGFbInZlcnNpb24iXSA9PSA5OgogICAgICAgICAgICBzZWxmLnNib3ggPSB7fQogICAgICAgICAgICBzZWxmLnJlc2JveCA9IHt9CiAgICAgICAgICAgIGZvciBpMSwgYmwgaW4gZGF0YVsic2JveCJdLml0ZW1zKCk6CiAgICAgICAgICAgICAgICBpMiA9IGJ5dGVzKFtpbnQoaSkgZm9yIGkgaW4gYmwuc3BsaXQoIiwiKV0pCiAgICAgICAgICAgICAgICBzZWxmLnNib3hbaTFdID0gaTIKICAgICAgICAgICAgICAgIHNlbGYucmVzYm94W2kyXSA9IGkxCiAgICAgICAgICAgIHNlbGYuZW5jb2RpbmdfdHlwZSA9IGRhdGFbImVuY29kaW5nX3R5cGUiXQogICAgICAgICAgICBpZiBkYXRhWyJlbmNvZGluZ190eXBlIl0gPT0gInBhY2tldCI6CiAgICAgICAgICAgICAgICBzZWxmLmVuY29kZSA9IHNlbGYuX19vcmdfZW5jb2RlCiAgICAgICAgICAgICAgICBzZWxmLmRlY29kZSA9IHNlbGYuX19vcmdfZGVjb2RlCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBzZWxmLmVuY29kZSA9IHNlbGYuX19zZXBfZW5jb2RlCiAgICAgICAgICAgICAgICBzZWxmLmRlY29kZSA9IHNlbGYuX19zZXBfZGVjb2RlCiAgICAgICAgICAgIHNlbGYuc3BlY2lhbF9leGNoYW5nZSA9IGRhdGFbInNwZWNpYWxfZXhjaGFuZ2UiXQogICAgICAgICAgICBzZWxmLnBlcmxlbmd0aCA9IGRhdGFbInBlcmxlbmd0aCJdCiAgICAgICAgICAgIGlmIGRhdGFbInNwZWNpYWxfZXhjaGFuZ2UiXToKICAgICAgICAgICAgICAgIHNlbGYuY2FjaGVkX2hhc2ggPSBzZWxmLl9fc3BlY2lhbF9leGNoYW5nZWRfY2FjaGVkX2hhc2gKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHNlbGYuY2FjaGVkX2hhc2ggPSBzZWxmLl9fb3JnX2NhY2hlZF9oYXNoCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcmFpc2UgVmFsdWVFcnJvcigiSW52YWxpZCB2ZXJzaW9uLiIpCgogICAgZGVmIGxvYWRfb25seV9lbmNvZGluZyhzZWxmLCBkYXRhKToKICAgICAgICBkYXRhID0ganNvbi5sb2FkcyhkYXRhKQogICAgICAgIGlmIGRhdGFbInZlcnNpb24iXSA9PSA5OgogICAgICAgICAgICBzZWxmLnNib3ggPSB7fQogICAgICAgICAgICBzZWxmLnJlc2JveCA9IHt9CiAgICAgICAgICAgIGZvciBpMSwgYmwgaW4gZGF0YVsic2JveCJdLml0ZW1zKCk6CiAgICAgICAgICAgICAgICBpMiA9IGJ5dGVzKFtpbnQoaSkgZm9yIGkgaW4gYmwuc3BsaXQoIiwiKV0pCiAgICAgICAgICAgICAgICBzZWxmLnNib3hbaTFdID0gaTIKICAgICAgICAgICAgICAgIHNlbGYucmVzYm94W2kyXSA9IGkxCiAgICAgICAgICAgIHNlbGYuZW5jb2RpbmdfdHlwZSA9IGRhdGFbImVuY29kaW5nX3R5cGUiXQogICAgICAgICAgICBzZWxmLnBlcmxlbmd0aCA9IGRhdGFbInBlcmxlbmd0aCJdCiAgICAgICAgICAgIGlmIGRhdGFbImVuY29kaW5nX3R5cGUiXSA9PSAicGFja2V0IjoKICAgICAgICAgICAgICAgIHNlbGYuZW5jb2RlID0gc2VsZi5fX29yZ19lbmNvZGUKICAgICAgICAgICAgICAgIHNlbGYuZGVjb2RlID0gc2VsZi5fX29yZ19kZWNvZGUKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHNlbGYuZW5jb2RlID0gc2VsZi5fX3NlcF9lbmNvZGUKICAgICAgICAgICAgICAgIHNlbGYuZGVjb2RlID0gc2VsZi5fX3NlcF9kZWNvZGUKICAgICAgICBlbHNlOgogICAgICAgICAgICByYWlzZSBWYWx1ZUVycm9yKCJJbnZhbGlkIHZlcnNpb24uIikKCiAgICBkZWYgYWRkaXYoc2VsZiwgZGF0YSwgbGVuZ3RoPTI1NiwgeGJhc2U9MSwgaW50ZXJ2YWw9MSk6ICAjIElWL25vbmNlIChJbml0aWFsaXphdGlvbiBWZWN0b3IpIEFkZCBJVgogICAgICAgIGtleSA9IG9zLnVyYW5kb20obGVuZ3RoKQogICAgICAgIHJldHVybiBrZXkgKyBzZWxmLmVuY3J5cHQoZGF0YSwga2V5LCB4YmFzZSwgaW50ZXJ2YWwpCgogICAgZGVmIGRlbGl2KHNlbGYsIGRhdGEsIGxlbmd0aD0yNTYsIHhiYXNlPTEsIGludGVydmFsPTEpOiAgIyBSZW1vdmUgSVYKICAgICAgICBrZXkgPSBkYXRhWzpsZW5ndGhdCiAgICAgICAgZGF0YSA9IGRhdGFbbGVuZ3RoOl0KICAgICAgICByZXR1cm4gc2VsZi5kZWNyeXB0KGRhdGEsIGtleSwgeGJhc2UsIGludGVydmFsKQ==" # LeCatchu v9 Cryptography Engine  
def lc():  
	global lc_code  
	space = {}  
	exec(base64.b64decode(lc_code.encode()).decode(), space, space)  
	return eval("LeCatchu_Engine", space, space)  
eng = lc()()  
"""  
code2="""codetarget = '$codetarget'  
exec(eng.decrypt_with_iv(base64.b64decode(codetarget.encode("utf-8")), $keytarget).decode("utf-8"))"""  
  
exec(code)  
  
def to_secure_code(target, count=4, keylength=64, addengcode=True, useb64=True):  
	global code, code2, eng  
	codes = []  
	print("Creating fake code parts...")
	for h in range(count):  
		passcode = " "*len(target)  
		keytarget = int("".join([str(random.randint(1, 9)) for _ in range(keylength)]))  
		c = base64.b64encode(eng.encrypt_with_iv(passcode.encode(), keytarget)).decode()  
		cc = code2.replace("$codetarget", c).replace("$keytarget", str(keytarget))  
		codes.append(cc)  
	print("Adding real code part...")
	keytarget = int("".join([str(random.randint(1, 9)) for _ in range(keylength)]))  
	c = base64.b64encode(eng.encrypt_with_iv(target.encode("utf-8"), keytarget)).decode()  
	cc = code2.replace("$codetarget", c).replace("$keytarget", str(keytarget))  
	codes.append(cc)  
	random.shuffle(codes)  
	c = code if addengcode else ""  
	c = c+"\n".join(codes)  
	if useb64:  
		c = base64.b64encode(c.encode()).decode()  
		return f"import base64;exec(base64.b64decode('{c}'.encode()).decode())"  
	else:  
		return c  
  
def encrypt_code(target, count=4, indent=0, keylength=64, perb64=True, endb64=True):  
	for i in range(indent):  
		print(f"Indent encrypting... {i+1}/{indent}")
		target = to_secure_code(target, count=count, keylength=keylength, addengcode=False, useb64=perb64)  
	print("Finish encryption...")
	return to_secure_code(target, count=count, keylength=keylength, addengcode=True, useb64=endb64)  
  
def rgb_to_ansi(r, g, b):
	return f"\033[38;2;{r};{g};{b}m"  
  
def print_colored_text(text, color1, color2):
	for i, h in enumerate(text):
		ind = i/len(text)
		isc = 0;r = color1[isc]+int((color2[isc]-color1[isc])*ind)
		isc = 1;g = color1[isc]+int((color2[isc]-color1[isc])*ind)
		isc = 2;b = color1[isc]+int((color2[isc]-color1[isc])*ind)
		sys.stdout.write(rgb_to_ansi(r, g, b)+h)
	sys.stdout.flush()

def print_advanced_colored_text(text):
	color1 = (0, 180, 255)
	color2 = (80, 255, 128)
	text = text.replace("..1", rgb_to_ansi(color1[0], color1[1], color1[2]))
	text = text.replace("..2", rgb_to_ansi(color2[0], color2[1], color2[2]))
	text = text.replace("..0", "\033[0m")
	while "..//" in text:
		backtext = text[:text.find("..//")]
		sys.stdout.write(backtext)
		text = text[text.find("..//")+4:]
		endtext = text[:text.find("//..")]
		print_colored_text(endtext, color1, color2)
		text = text[text.find("//..")+4:]
	sys.stdout.write(text)
	sys.stdout.flush()

def menu():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
	print_advanced_colored_text("""..//  _______                   ___ ___ 
 |   _   .-----.---.-.-----|   Y   |
 |.  |   |  _  |  _  |  _  |   1   |
 |.  |   |   __|___._|__   |\_   _/ 
 |:  1   |__|           |__| |:  |  
 |::.. . |                   |::.|  
 `-------'                   `---'  
                                    //..\n..1..//Opaqy//.. ..2- Advanced Python Obfuscation Tool..0\n\n..1[ ..201 ..1] ..2Obfuscate File\n..1[ ..202 ..1] ..2Information/Usage\n\n..1[ ..200 ..1] ..2Exit..0\n\n..1> ..2""")
	i = input()
	try:
		i = str(int(i))
	except:
		pass
	if i == "1":
		print_advanced_colored_text("..1Current directory path : ..2"+os.getcwd())
		print_advanced_colored_text("\n..1Target file path : ..2")
		filepath = input()
		print_advanced_colored_text("..1New file path : ..2")
		filepath2 = input()
		print_advanced_colored_text("..1Fake copy code count (e.g. 4) : ..2")
		try:
			count = int(input())
		except:
			count = 4
		print_advanced_colored_text("..1Obfuscation depth/indent (e.g. 1) : ..2")
		try:
			indent = int(input())
		except:
			indent = 1
		print_advanced_colored_text("..1Encryption key length (e.g. 64) : ..2")
		try:
			keylength = int(input())
		except:
			keylength = 2
		print_advanced_colored_text("..1Use base64 for per depth part (true/false) : ..2")
		try:
			perb64 = "t" in input().lower()
		except:
			perb64 = False
		print_advanced_colored_text("..1Use base64 for end of obfuscation (true/false) : ..2")
		try:
			endb64 = "t" in input().lower()
		except:
			endb64 = True
		try:
			print_advanced_colored_text("..1[ ~ ] ..2Reading code file content... ")
			with open(filepath, "r", encoding="utf-8") as f:
				c = f.read()
			print_advanced_colored_text(f"..2(old size: {len(c)})\n")
			print_advanced_colored_text("..1[ ~ ] ..2Encrypting and obfuscating...\n")
			c = encrypt_code(c, count=count, indent=indent, keylength=keylength, perb64=perb64, endb64=endb64)
			print_advanced_colored_text(f"..1[ ~ ] ..2Saving to new file... (new size: {len(c)})\n")
			with open(filepath2, "w", encoding="utf-8") as f:
				f.write(c)
			print_advanced_colored_text("..1[ + ] ..2Finished.\n\n..1[ Enter to continue ]")
		except Exception as e:
			print_advanced_colored_text(f"\n..1[ - ] ..2Finished. Exit with error: {e}\n\n..1[ Enter to continue ]")
		input()
	elif i == "2":
		print_advanced_colored_text("""\n..//============================================================================//..
..//                                 OPAQY                                        //..
..//                       Advanced Python Obfuscator                            //..
..//                   Powered by LeCatchu v9 (LehnCATH4)                   //..
..//============================================================================//..

..1Developer:               Simon Scap
..1Cryptographic Engine:    LeCatchu v9 - LehnCATH4 (2025)

..1What does it do?
..2OPAQY protects your Python scripts using multi-layered polymorphic 
encryption combined with decoy (fake) payloads. The output remains 
100% pure Python — no external dependencies, no compiled binaries.

..1Core Features:
..2• Custom high-entropy stream cipher (LeCatchu v9) based on BLAKE2b
..2• Dynamic per-run S-box generation + shuffling
..2• Multiple fake encrypted blobs (decoy payloads) to confuse analysts
..2• Multi-layer ("indent") encryption with optional per-layer base64 wrapping
..2• Built-in TAC (Tag Authentication Code) for integrity verification
..2• Extremely high resistance against static analysis and automated deobfuscators

..1Performance & Size Warning:
..2Warning: Indent (layers) greater than 1 can significantly slow down execution 
..2         startup time (each layer requires full decryption at runtime).
..2Warning: Every additional layer causes exponential size growth 
..2         (e.g., 1-2 layers can turn a 1 KB script into 500 KB–3 MB+).

..1Recommended Settings (Best Balance):
..2Fake copies count    : 4–128
..2Obfuscation depth    : 1–2     (avoid more than 2 unless necessary)
..2Key length           : 64–128
..2Per-layer base64     : False
..2Final base64         : True

..1Legal Notice:
..2This tool is intended for legitimate use only:
..2- Protecting your own intellectual property
..2- Educational purposes and security research
..2- Authorized red team / penetration testing exercises

..2Any malicious use is strictly prohibited and is the sole 
..2responsibility of the user.

..//============================================================================//..""")
		print_advanced_colored_text("\n\n..1[ Enter to continue ]")
		input()
	elif i == "0":
		return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="OPAQY - Advanced Polymorphic Python Obfuscator (LeCatchu v9 Engine)",
        epilog="Example: python opaqy.py input.py output.py -c 12 -d 1 -k 128 --no-per-b64"
    )

    parser.add_argument("input", nargs="?", help="Input Python file path")
    parser.add_argument("output", nargs="?", help="Output (obfuscated) file path")
    parser.add_argument("-c", "--count", type=int, default=4,
                        help="Number of fake/decoy code chunks (default: 4, recommended: 8-64)")
    parser.add_argument("-d", "--depth", type=int, default=1,
                        help="Obfuscation depth/layers (1-2 recommended, default: 1)")
    parser.add_argument("-k", "--keylength", type=int, default=64,
                        help="Key digit length (64-256, default: 64)")
    parser.add_argument("--per-b64", action="store_true", default=True, dest="perb64",
                        help="Enable base64 wrapping on intermediate layers (default: enabled)")
    parser.add_argument("--no-per-b64", action="store_false", dest="perb64",
                        help="Disable base64 on intermediate layers")
    parser.add_argument("--final-b64", action="store_true", default=True, dest="endb64",
                        help="Enable final base64 wrapper (default: enabled)")
    parser.add_argument("--no-final-b64", action="store_false", dest="endb64",
                        help="Disable final base64 wrapper")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode (minimal output)")
    parser.add_argument("--version", action="version", version="OPAQY v1.0 - LeCatchu v9 (2025)")

    args = parser.parse_args()

    if args.input and args.output:
        if not os.path.isfile(args.input):
            print(f"[!] Error: Input file not found: {args.input}")
            sys.exit(1)

        if args.depth > 3:
            print(f"[!] Warning: Depth {args.depth} will produce extremely large and slow output.")

        try:
            if not args.quiet:
                print("[~] Reading source file...")

            with open(args.input, "r", encoding="utf-8") as f:
                source = f.read()

            if not args.quiet:
                print(f"[+] Source loaded: {len(source):,} characters")
                print(f"[~] Starting obfuscation (depth={args.depth}, decoys={args.count}, keylen={args.keylength})...")

            start = time.time()
            result = encrypt_code(
                target=source,
                count=args.count,
                indent=args.depth,
                keylength=args.keylength,
                perb64=args.perb64,
                endb64=args.endb64
            )
            elapsed = time.time() - start

            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result)

            if not args.quiet:
                print(f"[+] Obfuscation complete!")
                print(f"[+] Output saved: {args.output}")
                print(f"[+] Final size: {len(result):,} characters")
                print(f"[+] Time taken: {elapsed:.2f} seconds")
            else:
                print(f"Done : {args.output}")

        except Exception as e:
            print(f"[!] Error: {e}")
            sys.exit(1)

    else:
        while True:
            choice = menu()
            if choice == 0:
                break
