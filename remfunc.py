#!/usr/bin/env python
# coding: utf-8

# In[6]:


class remfunc:
    
    import socket, pickle
    
    
    
    def start_server(host,port,debug = False):
        
        
        if debug == True:
            print ("Server is Listening.....")
        HOST = 'egger-donau.de'
        PORT = 9980
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:

            try:
                
                

                conn, addr = s.accept()
                if debug == True:
                    print ('Connected by', addr)

                size = None
                #conn.send(bytes("OK","utf-8"))
                #data_variable = pickle.loads(data)
                
                if debug == True:
                    print ("Waiting for data of size: " + str(int(size.decode("utf-8"))))
                    size = conn.recv(4096)
                    
                #conn.send(pickle.dumps(size))

                data = conn.recv(int(size.decode("utf-8")))
                
                code = pickle.loads(data)
                block = '\n'.join(code.splitlines()[:-1])
                
                result = None
                try:
                
                    result = exec(code)
                    
                except Exception as e:
                    
                    result = e
                
                    
                    

                resultsize = str(len(pickle.dumps(result,-1)))

                conn.send(pickle.dumps(resultsize))

                conn.send(result)
                
                if debug == True:
                    print ('Data received from client')


            except:
                if debug == True:
                    print("ERROR OR CLIENT DONE")
                pass
    

    class client:
        
        def __init__(self, HOST,PORT):
                
                self.HOST = HOST
                self.PORT = PORT
                self.init = True
       
            
        def do(self,code):
            
            import socket, pickle
            
            
            HOST = self.HOST
            PORT = self.PORT
                
            if self.init == False:
                
                raise RuntimeError("Client not initialized, create class instance with instancename = remfunc.client(HOST,PORT) first. You only need to do this once.")
            
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            
            try:
                
                s.connect((HOST,PORT))
                
            except:
                
                raise RuntimeError("Can not connect to server. Is it running? Is host " + HOST + " and port " + str(PORT) + " correct?")
                
                
            datatosend = code
            
            size = str(len(pickle.dumbs(datatosend,-1)))
            
            rsize = None
            result = None
            
            try:
                
                s.send(bytes(size,"utf-8"))
                
                
            except:
                
                raise RuntimeError("Error sending code size")
                
            try:
                
                s.send(pickle.dumps(datatosend))
                
            except:
                
                raise RuntimeError("Error sending code")
              
            
            while True:
                
                try:
                    
                    rsize = s.recv(4096)
                    
                except:
                    
                    raise RuntimeError("Error recieving result size")
                   
                
                try:
                    
                    result = pickle.loads(conn.recv(int(rsize.decode("utf-8"))))
                    return result
                
                except:
                    
                    raise RuntimeError("Error recieving result")
                    
                
                    
                    





                
                

            
            
            
            
            
        
        



 


# In[11]:


try:
    
    exec(print(bla))
    
except Exception as e:
    
    print(e)


# In[7]:





# In[ ]:





# In[ ]:





# In[ ]:




