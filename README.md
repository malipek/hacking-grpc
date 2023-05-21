# Hacking gRPC

* Run adb server

* Connect mobile device or launch emulator

* Run proxy, with HTTP/2 support

* Launch MobSF

* Run MobSF Dynamic Analyzer for application you'd like to test

* Export CA Certificate from proxy

* Run `prepare-crt.py` with CA certificate file as argument, for example:

```
python3 prepare-crt.py cacert.der
```

* Use output from command to push CA certificate in PEM format to the device, for example:

```
adb push cacert.pem /system/etc/security/cacerts/9a5ba575.0
```

* Begin instrumentation in MobFS to enable SSL Pinning bypass

* Shutdown the application on the device

* Set up global proxy to your custom proxy instance, using ADB, for example:

```
adb shell settings put global http_proxy 127.0.0.1:28888
```

For Android Studio Emulator loopback (127.0.0.1) doesn't work. Use your network card IP.

* Watch proxy for incoming requests from application. For Burp, remember to disable Intercept, so the traffic is not paused after each request and reply.

* Analyze traffic in history window

* Save body of gRPC responses and requests as raw or hex

## TODO decode gRPC
