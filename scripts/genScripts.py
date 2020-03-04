if __name__ == '__main__':
	with open("main.sh", "w+") as f:
		for l in (0.0001,0.0005):
			for a in (5,):
				for p in (7,9):
					for e in (50,):
						for data in (2,4,5,6):
							for first_layer in (6,8,10,12):
								for second_layer in (6,8,10,12,14,16):
									print(
										"python ../train.py -e %d -b 50 -l %.4f -g 0 -r 0.1 -a %d -p %d -m 1 -d ./save/mar4-0/ --model_path ./save/mar4-0/ --data %d --first_layer %d --second_layer %d --dont_save_data --no_detailed_summary"\
										%(e,l,a,p,data,first_layer,second_layer),
										end="\n", file=f)
