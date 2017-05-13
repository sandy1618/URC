#ifndef mathFunc_h
#define mathFunc_h
#include <Arduino.h>
class mathFunc{
	public:
		mathFunc(){};
		static constexpr float Pi = 3.14159;
		float degToRad(float _val){
			return ((_val*PI)/180);
		};
		float radToDegrees(float _val){
			return ((_val*180)/PI);
		};
		float toFloat(int _val){
			return((_val)/(10^7));
		};
		int toSteps(float _degrees, float _stepAngle){
			return (int)(_degrees/_stepAngle);
		};
		float calcGripperDistance(float distance, float stepsPer){
			return (distance*stepsPer);
		};
		int dutyCycletoMicroSeconds(int maxSeconds, int minSeconds, int dutyCycle){
			return map((dutyCycle*100),-100,100,maxSeconds,minSeconds);
		};
};
#endif
