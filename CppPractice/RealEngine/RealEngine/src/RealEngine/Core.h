#pragma once

#ifdef RE_PLATFORM_WINDOWS
	#ifdef RE_BUILD_DLL
		#define RE_API _declspec(dllexport)
	#else
		#define RE_API _declspec(dllimport)
	#endif
#else
	#error RealEngine only support windows
#endif
