# paw_detective

## Guidelines

### Training:
1. [Dataset configuration](./docs/dataset.md)
2. [Training model](./docs/dataset.md)


### Running


### References
1. [Towards Data Science](https://towardsdatascience.com/trian-yolov8-instance-segmentation-on-your-data-6ffa04b2debd)
2. [Ultralytics](https://docs.ultralytics.com/datasets/segment/)
3. [Learn OpenCV](https://learnopencv.com/train-yolov8-on-custom-dataset/)

# Machine Configurations
```bash
NVIDIA-SMI 515.105.01
Driver Version: 515.105.01
CUDA Version: 11.7
GPU: NVIDIA GeForce RTX 3070 Laptop GPU, 7982MiB
```

| Class                      	| Images 	| Instances 	| Box(P   	| R      	| mAP50  	| mAP50-95) 	| Mask(P  	| R      	| mAP50  	| mAP50-95) 	|
|----------------------------	|--------	|-----------	|---------	|--------	|--------	|-----------	|---------	|--------	|--------	|-----------	|
| all                        	| 2205   	| 2201      	| 0.0835  	| 0.238  	| 0.0712 	| 0.0616    	| 0.0834  	| 0.238  	| 0.0711 	| 0.0587    	|
| Abyssinian                 	| 2205   	| 58        	| 0.0512  	| 0.483  	| 0.0495 	| 0.0425    	| 0.0512  	| 0.483  	| 0.0495 	| 0.0386    	|
| Bengal                     	| 2205   	| 61        	| 0.0632  	| 0.0164 	| 0.0391 	| 0.0313    	| 0.0632  	| 0.0164 	| 0.0391 	| 0.0308    	|
| Birman                     	| 2205   	| 61        	| 0.0808  	| 0.885  	| 0.195  	| 0.158     	| 0.0808  	| 0.885  	| 0.195  	| 0.155     	|
| Bombay                     	| 2205   	| 66        	| 0.0801  	| 0.182  	| 0.0495 	| 0.0385    	| 0.0801  	| 0.182  	| 0.0495 	| 0.042     	|
| British_Shorthair          	| 2205   	| 62        	| 0.0289  	| 0.0323 	| 0.0233 	| 0.0201    	| 0.0289  	| 0.0323 	| 0.0233 	| 0.02      	|
| Egyptian_Mau               	| 2205   	| 48        	| 0.0379  	| 0.271  	| 0.041  	| 0.0363    	| 0.0379  	| 0.271  	| 0.041  	| 0.0354    	|
| Maine_Coon                 	| 2205   	| 55        	| 0.148   	| 0.491  	| 0.155  	| 0.142     	| 0.148   	| 0.491  	| 0.155  	| 0.133     	|
| Persian                    	| 2205   	| 58        	| 0.0934  	| 0.879  	| 0.195  	| 0.173     	| 0.0934  	| 0.879  	| 0.195  	| 0.163     	|
| Ragdoll                    	| 2205   	| 57        	| 0.106   	| 0.754  	| 0.199  	| 0.176     	| 0.106   	| 0.754  	| 0.199  	| 0.16      	|
| Russian_Blue               	| 2205   	| 52        	| 0       	| 0      	| 0.0244 	| 0.021     	| 0       	| 0      	| 0.0247 	| 0.0203    	|
| Siamese                    	| 2205   	| 62        	| 0.101   	| 0.403  	| 0.0818 	| 0.0719    	| 0.101   	| 0.403  	| 0.0816 	| 0.064     	|
| Sphynx                     	| 2205   	| 73        	| 0.0102  	| 0.0274 	| 0.0346 	| 0.0302    	| 0.0102  	| 0.0274 	| 0.0341 	| 0.0281    	|
| american_bulldog           	| 2205   	| 61        	| 0.163   	| 0.0492 	| 0.0849 	| 0.0699    	| 0.163   	| 0.0492 	| 0.0849 	| 0.0713    	|
| american_pit_bull_terrier  	| 2205   	| 55        	| 0.0471  	| 0.291  	| 0.0573 	| 0.0435    	| 0.0471  	| 0.291  	| 0.0573 	| 0.0434    	|
| basset_hound               	| 2205   	| 59        	| 0.119   	| 0.695  	| 0.153  	| 0.142     	| 0.119   	| 0.695  	| 0.153  	| 0.131     	|
| beagle                     	| 2205   	| 60        	| 0.114   	| 0.0833 	| 0.0682 	| 0.0542    	| 0.114   	| 0.0833 	| 0.0682 	| 0.0544    	|
| boxer                      	| 2205   	| 56        	| 0.083   	| 0.482  	| 0.101  	| 0.0869    	| 0.08    	| 0.464  	| 0.0989 	| 0.083     	|
| chihuahua                  	| 2205   	| 65        	| 0.0138  	| 0.0308 	| 0.0459 	| 0.0395    	| 0.0138  	| 0.0308 	| 0.0459 	| 0.0363    	|
| english_cocker_spaniel     	| 2205   	| 73        	| 0       	| 0      	| 0.0377 	| 0.0335    	| 0       	| 0      	| 0.0377 	| 0.0317    	|
| english_setter             	| 2205   	| 54        	| 0.0293  	| 0.167  	| 0.0361 	| 0.0314    	| 0.0293  	| 0.167  	| 0.0361 	| 0.0303    	|
| german_shorthaired         	| 2205   	| 68        	| 0.0923  	| 0.426  	| 0.106  	| 0.0921    	| 0.0923  	| 0.426  	| 0.106  	| 0.0875    	|
| great_pyrenees             	| 2205   	| 57        	| 0.0106  	| 0.0175 	| 0.0347 	| 0.0301    	| 0.0106  	| 0.0175 	| 0.0347 	| 0.0298    	|
| havanese                   	| 2205   	| 49        	| 0.0847  	| 0.245  	| 0.0534 	| 0.0451    	| 0.0847  	| 0.245  	| 0.0534 	| 0.0453    	|
| japanese_chin              	| 2205   	| 54        	| 0       	| 0      	| 0.0298 	| 0.0257    	| 0       	| 0      	| 0.0298 	| 0.0235    	|
| keeshond                   	| 2205   	| 67        	| 0.119   	| 0.0149 	| 0.0459 	| 0.0417    	| 0.119   	| 0.0149 	| 0.0459 	| 0.0399    	|
| leonberger                 	| 2205   	| 58        	| 0.00729 	| 0.0172 	| 0.0279 	| 0.0257    	| 0.00729 	| 0.0172 	| 0.0279 	| 0.0239    	|
| miniature_pinscher         	| 2205   	| 50        	| 0.0656  	| 0.26   	| 0.0811 	| 0.0672    	| 0.0656  	| 0.26   	| 0.0811 	| 0.0626    	|
| newfoundland               	| 2205   	| 65        	| 0       	| 0      	| 0.0449 	| 0.0392    	| 0       	| 0      	| 0.0445 	| 0.0398    	|
| pomeranian                 	| 2205   	| 52        	| 0.0622  	| 0.462  	| 0.056  	| 0.0483    	| 0.0622  	| 0.462  	| 0.056  	| 0.0428    	|
| pug                        	| 2205   	| 62        	| 1       	| 0      	| 0.0629 	| 0.0579    	| 1       	| 0      	| 0.0629 	| 0.053     	|
| saint_bernard              	| 2205   	| 61        	| 0.059   	| 0.197  	| 0.0525 	| 0.0462    	| 0.059   	| 0.197  	| 0.0525 	| 0.0451    	|
| samoyed                    	| 2205   	| 64        	| 0.0965  	| 0.484  	| 0.11   	| 0.0939    	| 0.0965  	| 0.484  	| 0.11   	| 0.0903    	|
| scottish_terrier           	| 2205   	| 55        	| 0.0559  	| 0.309  	| 0.06   	| 0.0537    	| 0.0559  	| 0.309  	| 0.06   	| 0.0523    	|
| shiba_inu                  	| 2205   	| 60        	| 0.0283  	| 0.117  	| 0.0336 	| 0.0292    	| 0.0283  	| 0.117  	| 0.0336 	| 0.0277    	|
| staffordshire_bull_terrier 	| 2205   	| 58        	| 0       	| 0      	| 0.0801 	| 0.0693    	| 0       	| 0      	| 0.0801 	| 0.0665    	|
| wheaten_terrier            	| 2205   	| 62        	| 0       	| 0      	| 0.0459 	| 0.0379    	| 0       	| 0      	| 0.0446 	| 0.0371    	|
| yorkshire_terrier          	| 2205   	| 63        	| 0.0398  	| 0.0476 	| 0.0412 	| 0.0341    	| 0.0398  	| 0.0476 	| 0.0412 	| 0.0338    	|
