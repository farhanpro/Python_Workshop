import speedtest
st = speedtest.Speedtest()
option = int(input("What do you want to test:\n1) Download Speed \n2) Upload Speed \n3) Ping \n :"))
if option == 1:
    print(st.download())
elif option == 2:
    print((st.upload()))
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping) 
else:
    print("Invalid Input")