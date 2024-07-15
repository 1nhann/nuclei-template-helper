from nuclei import BaseHTTP,Template
http = BaseHTTP(method="POST")
http.set_paths(
    paths=[
        '{{BaseURL}}/runtime/log/{{date_time("%Y%M")}}/{{date_time(%D)}}.log',
        '{{BaseURL}}/runtime/log/{{date_time("%Y%M")}}/{{date_time(%D)}}_cli.log',
        '{{BaseURL}}/runtime/log/{{date_time("%Y%M")}}/{{date_time(%D)}}_error.log',
        '{{BaseURL}}/runtime/log/{{date_time("%Y%M")}}/{{date_time(%D)}}_sql.log',
    ]
)
http.set_status_matcher(
    [200]
)
http.dump(
    id="ThinkPHP 5.x 日志泄露",
    fingers=[
        "thinkphp"
    ]
)