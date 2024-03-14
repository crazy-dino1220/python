import network


wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)

wifi_list = wlan.scan()
print("Scan result:")
for i in range(len(wifi_list)):
    print(wifi_list[i])
wlSSID = "SingularClass"
wlPWD = "Singular#1234"
wlan.connect(wlSSID, wlPWD)
while not (wlan.isconnected()):
    pass
print("connet successfully", wlan.ifconfig())
