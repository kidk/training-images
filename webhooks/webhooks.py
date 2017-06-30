import re, subprocess, time, os
from threading import Thread
from flask import Flask, request

app = Flask(__name__)

@app.route('/debug/heapdump', methods=['POST'])
def debug_heapdump():
    content = request.get_json(force=True)

    if content.get('token') != '8d8efa2f-5fde-4d08-bb2d-6d227439e399':
        return "No valid token provided", 403

    if 'server' not in content:
        return "No server provided", 409

    if 'action' in content and content['action'] == 'triggered':
        pod = re.search('k8s_(.*)_(.*)_(.*)_(.*)', content['server']).group(2)
        take_heapdump(pod)
        return "Started heapdump for pod %s" % pod, 200
    else:
        return "Nothing to do here", 200


def take_heapdump(pod):
    filename     = '%s-%d.bin' % (pod, time.time())
    get_java_pid = 'ps aux | grep java | grep -v grep | awk "{ print \$2; }"'
    take_dump    = 'jmap -dump:format=b,file=%s $(%s)' % (filename, get_java_pid)
    upload_dump  = 'curl -T %s %s' % (filename, os.environ.get("FTP_URL"))
    cleanup      = 'rm %s' % filename

    cmd = 'cd tmp; %s && %s ; %s' % (take_dump, upload_dump, cleanup)

    t = Thread(target=subprocess.run , args=(["kubectl", "exec", pod, "--", "/bin/bash", "-c", cmd],))
    t.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
