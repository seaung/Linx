import socket
import ssl
import urllib.request


if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context


def BasicAuthCredentials(creds):
    return tuple(creds.split(":"))


def ProxiesHandler(proxy):
    return {"http": proxy, "https": proxy}


class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        pass

    http_error_302 = http_error_302 = http_error_302 = http_error_302


class Response(object):
    def __init__(self, response):
        self.body = response.read()
        self.url = response.geturl()
        self.status_code = response.getcode()
        self.headers = response.headers.dict


class Requests(object):
    def httpClient(self, 
            url, 
            method="GET", 
            data=None, 
            cookie=None,
            headers=None, 
            auth=None, 
            proxies=None, 
            timeout=None, 
            redirect=True, agent=None):

        if headers is None:
            headers = {}

        if auth is None:
            auth = ()

        if "User-Agent" not in headers:
            headers["User-Agent"] = agent

        if auth != None and auth != ():
            if ":" in auth:
                authentization = ("%s:%s" % (BasicAuthCredentials(auth))).encode("base64")
                headers["Authorization"] = "Basic %s" % (authentization.replace("\n", ""))

        if timeout != None:
            socket.setdefaulttimeout(timeout)

        handlers = [urllib.request.HTTPHandler(), urllib.request.HTTPSHandler()]

        if "Cookie" not in headers:
            if cookie != None and cookie != "":
                headers["Cookie"] = cookie

        if redirect != True:
            handlers.append(RedirectHandler)

        if proxies:
            proxy = ProxiesHandler(proxies)
            handlers.append(urllib.request.ProxyHandler(proxy))

        opener = urllib.request.build_opener(*handlers)
        urllib.request.install_opener(opener)

        if method == "GET":
            if data:
                url = "%s?%s" % (url, data)
                request = urllib.request.Request(url, headers=headers)
        elif method == "POST":
            request = urllib.request.Request(url, data=data, headers=headers)
        else:
            request = urllib.request.Request(url, headers=headers)
            request.get_method = lambda : method

        try:
            response = urllib.request.urlopen(request)
        except urllib.request.HTTPError as e:
            response = e
        except socket.error as e:
            exit(0)
        except urllib.request.URLError as e:
            exit(0)
        return Response(response)

