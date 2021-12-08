import logging
import mathart

def main():
	logging.basicConfig(filename='test.log', 
        filemode='w', 
        level=logging.INFO, 
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
	logging.info("Started")
	mathart.hexagonspiral()
	logging.info("Finished")

if __name__ == '__main__':
	main()
