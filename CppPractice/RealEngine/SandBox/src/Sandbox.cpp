#include "RealEngine.h"

class SandBox :public RealEngine::Application 
{
public:
	SandBox() 
	{

	}
	~SandBox() 
	{
	
	
	}
};

int main()
{
	SandBox* mySandBox_p = new SandBox();
	mySandBox_p->Run();
	delete mySandBox_p;

}