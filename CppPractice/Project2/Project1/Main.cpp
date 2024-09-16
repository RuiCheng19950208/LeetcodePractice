
#include "MyHeader.h"
#include "Log.cpp"
#include "Print.cpp"



int main(){
	Log myLog;
	myLog.set_log_mode(myLog.Log_mode_warn);
	myLog.Warning("Hello World");
	myLog.set_log_mode(myLog.Log_mode_message);
	myLog.Message("Hello World");

	Print myPrint;
	myPrint.print(5);
	myPrint.print(5.5);
	myPrint.print("Hello World");

	map<string, int> myMap;
	myMap["dasima"] = 1;
	myMap["ruicheng"] = 2;
	myMap["kaka"] = 3;
	for (map<string,int>::iterator it=myMap.begin();it!=myMap.end();it++)
	{
		cout << it->first << endl;
		cout << it->second << endl;

	}

}