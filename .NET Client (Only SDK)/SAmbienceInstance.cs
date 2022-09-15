public class SAmbienceInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __Update(float fxCenter, float fyCenter, float fzCenter)
	{
		if (0 == dwRange)
		{
			return;
		}
    
		Update(fxCenter, fyCenter, fzCenter);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateOnceSound(float fxCenter, float fyCenter, float fzCenter)
	{
		float fDistance = sqrtf((fx - fxCenter) * (fx - fxCenter) + (fy - fyCenter) * (fy - fyCenter) + (fz - fzCenter) * (fz - fzCenter));
		if ((uint)fDistance < dwRange)
		{
			if (-1 == iPlaySoundIndex)
			{
				if (AmbienceData.AmbienceSoundVector.empty())
				{
					return;
				}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				char c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				iPlaySoundIndex = CSoundManager.Instance().PlayAmbienceSound3D(fx, fy, fz, c_szFileName);
			}
		}
		else
		{
			iPlaySoundIndex = -1;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateStepSound(float fxCenter, float fyCenter, float fzCenter)
	{
		float fDistance = sqrtf((fx - fxCenter) * (fx - fxCenter) + (fy - fyCenter) * (fy - fyCenter) + (fz - fzCenter) * (fz - fzCenter));
		if ((uint)fDistance < dwRange)
		{
			float fcurTime = CTimer.Instance().GetCurrentSecond();
    
			if (fcurTime > fNextPlayTime)
			{
				if (AmbienceData.AmbienceSoundVector.empty())
				{
					return;
				}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				char c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				iPlaySoundIndex = CSoundManager.Instance().PlayAmbienceSound3D(fx, fy, fz, c_szFileName);
    
				fNextPlayTime = CTimer.Instance().GetCurrentSecond();
				fNextPlayTime += AmbienceData.fPlayInterval + frandom(0.0f, AmbienceData.fPlayIntervalVariation);
			}
		}
		else
		{
			iPlaySoundIndex = -1;
			fNextPlayTime = 0.0f;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateLoopSound(float fxCenter, float fyCenter, float fzCenter)
	{
		float fDistance = sqrtf((fx - fxCenter) * (fx - fxCenter) + (fy - fyCenter) * (fy - fyCenter) + (fz - fzCenter) * (fz - fzCenter));
		if ((uint)fDistance < dwRange)
		{
			if (-1 == iPlaySoundIndex)
			{
				if (AmbienceData.AmbienceSoundVector.empty())
				{
					return;
				}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				char c_szFileName = AmbienceData.AmbienceSoundVector[0].c_str();
				iPlaySoundIndex = CSoundManager.Instance().PlayAmbienceSound3D(fx, fy, fz, c_szFileName, 0);
			}
    
			if (-1 != iPlaySoundIndex)
			{
				CSoundManager.Instance().SetSoundVolume3D(iPlaySoundIndex, __GetVolumeFromDistance(fDistance));
			}
		}
		else
		{
			if (-1 != iPlaySoundIndex)
			{
				CSoundManager.Instance().StopSound3D(iPlaySoundIndex);
				iPlaySoundIndex = -1;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float __GetVolumeFromDistance(float fDistance)
	{
		float fMaxVolumeAreaRadius = (float)dwRange * fMaxVolumeAreaPercentage;
		if (fMaxVolumeAreaRadius <= 0.0f)
		{
			return 1.0f;
		}
		if (fDistance <= fMaxVolumeAreaRadius)
		{
			return 1.0f;
		}
    
		return 1.0f - ((fDistance - fMaxVolumeAreaRadius) / (dwRange - fMaxVolumeAreaRadius));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Render()
	{
		float fBoxSize = 10.0f;
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, 0xff00ff00);
		RenderCube(fx - fBoxSize, fy - fBoxSize, fz - fBoxSize, fx + fBoxSize, fy + fBoxSize, fz + fBoxSize);
		(CStateManager.Instance()).SetRenderState(D3DRS_TEXTUREFACTOR, 0xffffffff);
		RenderSphere(null, fx, fy, fz, (float)dwRange * fMaxVolumeAreaPercentage, D3DFILL_POINT);
		RenderSphere(null, fx, fy, fz, (float)dwRange, D3DFILL_POINT);
		RenderCircle2d(fx, fy, fz, (float)dwRange * fMaxVolumeAreaPercentage);
		RenderCircle2d(fx, fy, fz, (float)dwRange);
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < 4; ++i)
		{
			float fxAdd = cosf((float)i * ((float) 3.141592654f) / 4.0f) * (float)dwRange / 2.0f;
			float fyAdd = sinf((float)i * ((float) 3.141592654f) / 4.0f) * (float)dwRange / 2.0f;
    
			if ((i % 2) != 0)
			{
				fxAdd /= 2.0f;
				fyAdd /= 2.0f;
			}
    
			RenderLine2d(fx + fxAdd, fy + fyAdd, fx - fxAdd, fy - fyAdd, fz);
		}
	}
}