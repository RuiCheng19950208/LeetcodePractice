#include "MyHeader.h"



class Log
{
private:
	int Log_mode = Log_mode_message;
public:
	const int Log_mode_error = 0;
	const int Log_mode_warn = 1;
	const int Log_mode_message = 2;

	void set_log_mode(int mode)
	{
		Log_mode = mode;
	}
	void Warning(const char* message)
	{

		if (Log_mode == Log_mode_warn)
		{
			cout << "[Warning]: " << message << endl;
		}
	}
	void Error(const char* message)
	{
		if (Log_mode == Log_mode_error)
		{
			cout << "[Error]: " << message << endl;
		}

	}
	void Message(const char* message)
	{
		if (Log_mode == Log_mode_message)
		{
			cout << "[Message]: " << message << endl;
		}
	}


};
