public class SGroundItemInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Clear()
	{
		stOwnership = "";
		ThingInstance.Clear();
		CEffectManager.Instance().DestroyEffectInstance(dwEffectInstanceIndex);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PlayDropSound(uint eItemType, in _D3DVECTOR c_rv3Pos)
	{
		if (eItemType >= DROPSOUND_NUM)
		{
			return;
		}
    
		CSoundManager.Instance().PlaySound3D(c_rv3Pos.x, c_rv3Pos.y, c_rv3Pos.z, ms_astDropSoundFileName[eItemType].c_str());
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool Update()
	{
		if (bAnimEnded)
		{
			return false;
		}
		if (dwEndTime < CTimer.Instance().GetCurrentMillisecond())
		{
			ThingInstance.SetRotationQuaternion(qEnd);
    
			D3DXQUATERNION qAdjust = new D3DXQUATERNION(-v3Center.x, -v3Center.y, -v3Center.z, 0.0f);
			D3DXQUATERNION qc = new D3DXQUATERNION();
			D3DXQuaternionConjugate(qc, qEnd);
			D3DXQuaternionMultiply(qAdjust, qAdjust, qEnd);
			D3DXQuaternionMultiply(qAdjust, qc, qAdjust);
    
			ThingInstance.SetPosition(v3EndPosition.x + qAdjust.x, v3EndPosition.y + qAdjust.y, v3EndPosition.z + qAdjust.z);
    
			bAnimEnded = true;
    
			__PlayDropSound(eDropSoundType, v3EndPosition);
		}
		else
		{
			uint time = CTimer.Instance().GetCurrentMillisecond() - dwStartTime;
			uint etime = dwEndTime - CTimer.Instance().GetCurrentMillisecond();
			float rate = time * 1.0f / (dwEndTime - dwStartTime);
    
			_D3DVECTOR v3NewPosition = v3EndPosition;
			v3NewPosition.z += 100 - 100 * rate * (3 * rate-2);
    
			D3DXQUATERNION q = new D3DXQUATERNION();
			D3DXQuaternionRotationAxis(q, v3RotationAxis, etime * 0.03f * (-1 + rate * (3 * rate-2)));
			D3DXQuaternionMultiply(q, qEnd, q);
    
			ThingInstance.SetRotationQuaternion(q);
			D3DXQUATERNION qAdjust = new D3DXQUATERNION(-v3Center.x, -v3Center.y, -v3Center.z, 0.0f);
			D3DXQUATERNION qc = new D3DXQUATERNION();
			D3DXQuaternionConjugate(qc, q);
			D3DXQuaternionMultiply(qAdjust, qAdjust, q);
			D3DXQuaternionMultiply(qAdjust, qc, qAdjust);
    
			ThingInstance.SetPosition(v3NewPosition.x + qAdjust.x, v3NewPosition.y + qAdjust.y, v3NewPosition.z + qAdjust.z);
    
		}
		ThingInstance.Transform();
		ThingInstance.Deform();
		return !bAnimEnded;
	}
}