public class CBaseCollisionInstance
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public CBaseCollisionInstance BuildCollisionInstance(CStaticCollisionData c_pCollisionData, _D3DMATRIX pMat)
	{
		switch (c_pCollisionData.dwType)
		{
			case COLLISION_TYPE_PLANE:
			{
					CPlaneCollisionInstance ppci = gs_pci.Alloc();
					_D3DMATRIX matRotation = new _D3DMATRIX();
					_D3DMATRIX matTranslationLocal = new _D3DMATRIX();
					D3DXMatrixRotationQuaternion(matRotation, c_pCollisionData.quatRotation);
					D3DXMatrixTranslation(matTranslationLocal, c_pCollisionData.v3Position.x, c_pCollisionData.v3Position.y, c_pCollisionData.v3Position.z);
					_D3DMATRIX matTransform = matRotation * matTranslationLocal * pMat;
    
					SPlaneData PlaneData = ppci.GetAttribute();
					D3DXVec3TransformCoord(PlaneData.v3Position, c_pCollisionData.v3Position, pMat);
					float fHalfWidth = c_pCollisionData.fDimensions[0] / 2.0f;
					float fHalfLength = c_pCollisionData.fDimensions[1] / 2.0f;
    
					PlaneData.v3QuadPosition[0].x = -fHalfWidth;
					PlaneData.v3QuadPosition[0].y = -fHalfLength;
					PlaneData.v3QuadPosition[0].z = 0.0f;
					PlaneData.v3QuadPosition[1].x = +fHalfWidth;
					PlaneData.v3QuadPosition[1].y = -fHalfLength;
					PlaneData.v3QuadPosition[1].z = 0.0f;
					PlaneData.v3QuadPosition[2].x = -fHalfWidth;
					PlaneData.v3QuadPosition[2].y = +fHalfLength;
					PlaneData.v3QuadPosition[2].z = 0.0f;
					PlaneData.v3QuadPosition[3].x = +fHalfWidth;
					PlaneData.v3QuadPosition[3].y = +fHalfLength;
					PlaneData.v3QuadPosition[3].z = 0.0f;
					for (uint LaniatusDefVariables = 0; LaniatusDefVariables < 4; ++i)
					{
						D3DXVec3TransformCoord(PlaneData.v3QuadPosition[i], PlaneData.v3QuadPosition[i], matTransform);
					}
					_D3DVECTOR v3Line0 = PlaneData.v3QuadPosition[1] - PlaneData.v3QuadPosition[0];
					_D3DVECTOR v3Line1 = PlaneData.v3QuadPosition[2] - PlaneData.v3QuadPosition[0];
					_D3DVECTOR v3Line2 = PlaneData.v3QuadPosition[1] - PlaneData.v3QuadPosition[3];
					_D3DVECTOR v3Line3 = PlaneData.v3QuadPosition[2] - PlaneData.v3QuadPosition[3];
					D3DXVec3Normalize(v3Line0, v3Line0);
					D3DXVec3Normalize(v3Line1, v3Line1);
					D3DXVec3Normalize(v3Line2, v3Line2);
					D3DXVec3Normalize(v3Line3, v3Line3);
					D3DXVec3Cross(PlaneData.v3Normal, v3Line0, v3Line1);
					D3DXVec3Normalize(PlaneData.v3Normal, PlaneData.v3Normal);
    
					D3DXVec3Cross(PlaneData.v3InsideVector[0], PlaneData.v3Normal, v3Line0);
					D3DXVec3Cross(PlaneData.v3InsideVector[1], v3Line1, PlaneData.v3Normal);
					D3DXVec3Cross(PlaneData.v3InsideVector[2], v3Line2, PlaneData.v3Normal);
					D3DXVec3Cross(PlaneData.v3InsideVector[3], PlaneData.v3Normal, v3Line3);
    
					return ppci;
			}
				break;
			case COLLISION_TYPE_BOX:
				Debug.Assert(false && "COLLISION_TYPE_BOX not implemented");
				break;
			case COLLISION_TYPE_AABB:
			{
					CAABBCollisionInstance paci = gs_aci.Alloc();
    
					_D3DMATRIX matTranslationLocal = new _D3DMATRIX();
					D3DXMatrixTranslation(matTranslationLocal, c_pCollisionData.v3Position.x, c_pCollisionData.v3Position.y, c_pCollisionData.v3Position.z);
					_D3DMATRIX matTransform = new _D3DMATRIX(pMat);
    
					_D3DVECTOR v3Pos = new _D3DVECTOR();
					v3Pos.x = matTranslationLocal._41;
					v3Pos.y = matTranslationLocal._42;
					v3Pos.z = matTranslationLocal._43;
    
					SAABBData AABBData = paci.GetAttribute();
					AABBData.v3Min.x = v3Pos.x - c_pCollisionData.fDimensions[0];
					AABBData.v3Min.y = v3Pos.y - c_pCollisionData.fDimensions[1];
					AABBData.v3Min.z = v3Pos.z - c_pCollisionData.fDimensions[2];
					AABBData.v3Max.x = v3Pos.x + c_pCollisionData.fDimensions[0];
					AABBData.v3Max.y = v3Pos.y + c_pCollisionData.fDimensions[1];
					AABBData.v3Max.z = v3Pos.z + c_pCollisionData.fDimensions[2];
    
					D3DXVec3TransformCoord(AABBData.v3Min, AABBData.v3Min, matTransform);
					D3DXVec3TransformCoord(AABBData.v3Max, AABBData.v3Max, matTransform);
    
					return paci;
			}
				break;
				case COLLISION_TYPE_OBB:
				{
					COBBCollisionInstance poci = gs_oci.Alloc();
    
					_D3DMATRIX matTranslationLocal = new _D3DMATRIX();
					D3DXMatrixTranslation(matTranslationLocal, c_pCollisionData.v3Position.x, c_pCollisionData.v3Position.y, c_pCollisionData.v3Position.z);
					_D3DMATRIX matRotation = new _D3DMATRIX();
					D3DXMatrixRotationQuaternion(matRotation, c_pCollisionData.quatRotation);
    
					_D3DMATRIX matTranslationWorld = new _D3DMATRIX();
					D3DXMatrixIdentity(matTranslationWorld);
					matTranslationWorld._41 = pMat._41;
					matTranslationWorld._42 = pMat._42;
					matTranslationWorld._43 = pMat._43;
					matTranslationWorld._44 = pMat._44;
    
					_D3DVECTOR v3Min = new _D3DVECTOR();
					_D3DVECTOR v3Max = new _D3DVECTOR();
					v3Min.x = c_pCollisionData.v3Position.x - c_pCollisionData.fDimensions[0];
					v3Min.y = c_pCollisionData.v3Position.y - c_pCollisionData.fDimensions[1];
					v3Min.z = c_pCollisionData.v3Position.z - c_pCollisionData.fDimensions[2];
					v3Max.x = c_pCollisionData.v3Position.x + c_pCollisionData.fDimensions[0];
					v3Max.y = c_pCollisionData.v3Position.y + c_pCollisionData.fDimensions[1];
					v3Max.z = c_pCollisionData.v3Position.z + c_pCollisionData.fDimensions[2];
    
					D3DXVec3TransformCoord(v3Min, v3Min, pMat);
					D3DXVec3TransformCoord(v3Max, v3Max, pMat);
					_D3DVECTOR v3Position = (v3Min + v3Max) * 0.5f;
    
					SOBBData OBBData = poci.GetAttribute();
					OBBData.v3Min.x = v3Position.x - c_pCollisionData.fDimensions[0];
					OBBData.v3Min.y = v3Position.y - c_pCollisionData.fDimensions[1];
					OBBData.v3Min.z = v3Position.z - c_pCollisionData.fDimensions[2];
					OBBData.v3Max.x = v3Position.x + c_pCollisionData.fDimensions[0];
					OBBData.v3Max.y = v3Position.y + c_pCollisionData.fDimensions[1];
					OBBData.v3Max.z = v3Position.z + c_pCollisionData.fDimensions[2];
    
    
    
					_D3DMATRIX matTransform = new _D3DMATRIX(pMat);
    
					D3DXMatrixIdentity(OBBData.matRot);
					OBBData.matRot = pMat;
					OBBData.matRot._41 = 0;
					OBBData.matRot._42 = 0;
					OBBData.matRot._43 = 0;
					OBBData.matRot._44 = 1;
    
    
    
    
					return poci;
				}
				break;
			case COLLISION_TYPE_SPHERE:
			{
					CSphereCollisionInstance psci = gs_sci.Alloc();
    
					_D3DMATRIX matTranslationLocal = new _D3DMATRIX();
					D3DXMatrixTranslation(matTranslationLocal, c_pCollisionData.v3Position.x, c_pCollisionData.v3Position.y, c_pCollisionData.v3Position.z);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matTranslationLocal = matTranslationLocal **pMat;
					matTranslationLocal.CopyFrom(matTranslationLocal * pMat);
    
					SSphereData SphereData = psci.GetAttribute();
					SphereData.v3Position.x = matTranslationLocal._41;
					SphereData.v3Position.y = matTranslationLocal._42;
					SphereData.v3Position.z = matTranslationLocal._43;
					SphereData.fRadius = c_pCollisionData.fDimensions[0];
    
					return psci;
			}
				break;
			case COLLISION_TYPE_CYLINDER:
			{
					CCylinderCollisionInstance pcci = gs_cci.Alloc();
    
					_D3DMATRIX matTranslationLocal = new _D3DMATRIX();
					D3DXMatrixTranslation(matTranslationLocal, c_pCollisionData.v3Position.x, c_pCollisionData.v3Position.y, c_pCollisionData.v3Position.z);
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: matTranslationLocal = matTranslationLocal **pMat;
					matTranslationLocal.CopyFrom(matTranslationLocal * pMat);
    
					SCylinderData CylinderData = pcci.GetAttribute();
					CylinderData.fRadius = c_pCollisionData.fDimensions[0];
					CylinderData.fHeight = c_pCollisionData.fDimensions[1];
					CylinderData.v3Position.x = matTranslationLocal._41;
					CylinderData.v3Position.y = matTranslationLocal._42;
					CylinderData.v3Position.z = matTranslationLocal._43;
    
					return pcci;
			}
				break;
		}
		Debug.Assert(false && "NOT_REACHED");
		return null;
	}
}