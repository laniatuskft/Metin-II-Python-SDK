//# Laniatus Games Studio Inc. |: C# has no need of forward class declarations:
//class CInstanceBase;

#if ENABLE_LOAD_PLAYERSETTING
namespace NPlayerData
{

	public enum EEmotions
	{
		EMOTION_CLAP = 1,
		EMOTION_CONGRATULATION,
		EMOTION_FORGIVE,
		EMOTION_ANGRY,
		EMOTION_ATTRACTIVE,
		EMOTION_SAD,
		EMOTION_SHY,
		EMOTION_CHEERUP,
		EMOTION_BANTER,
		EMOTION_JOY,
		EMOTION_CHEERS_1,
		EMOTION_CHEERS_2,
		EMOTION_DANCE_1,
		EMOTION_DANCE_2,
		EMOTION_DANCE_3,
		EMOTION_DANCE_4,
		EMOTION_DANCE_5,
		EMOTION_DANCE_6,
		EMOTION_KISS = 51,
		EMOTION_FRENCH_KISS,
		EMOTION_SLAP
	}
}
#endif

public class IAbstractPlayer : TAbstractSingleton<IAbstractPlayer>
{
		public IAbstractPlayer()
		{
		}
		public virtual void Dispose()
		{
		}

		public abstract uint GetMainCharacterIndex();
		public abstract void SetMainCharacterIndex(int iIndex);
		public abstract bool IsMainCharacterIndex(uint dwIndex);

		public abstract long GetStatus(uint dwType);

		public abstract string GetName();

		public abstract void SetRace(uint dwRace);

		public abstract void StartStaminaConsume(uint dwConsumePerSec, uint dwCurrentStamina);
		public abstract void StopStaminaConsume(uint dwCurrentStamina);

		public abstract bool IsPartyMemberByVID(uint dwVID);
		public abstract bool PartyMemberVIDToPID(uint dwVID, ref uint pdwPID);
		public abstract bool IsSamePartyMember(uint dwVID1, uint dwVID2);

		public abstract void SetItemData(TItemPos itemPos, in TItemData c_rkItemInst);
		public abstract void SetItemCount(TItemPos itemPos, ushort wCount);
		public abstract void SetItemMetinSocket(TItemPos itemPos, uint dwMetinSocketIndex, uint dwMetinNumber);
		public abstract void SetItemAttribute(TItemPos itemPos, uint dwAttrIndex, byte byType, short sValue);

		public abstract uint GetItemIndex(TItemPos itemPos);
		public abstract uint GetItemFlags(TItemPos itemPos);
		public abstract uint GetItemCount(TItemPos itemPos);

		public abstract bool IsEquipItemInSlot(TItemPos itemPos);

		public abstract void AddQuickSlot(int QuickslotIndex, char IconType, char IconPosition);
		public abstract void DeleteQuickSlot(int QuickslotIndex);
		public abstract void MoveQuickSlot(int Source, int Target);

		public abstract void SetWeaponPower(uint dwMinPower, uint dwMaxPower, uint dwMinMagicPower, uint dwMaxMagicPower, uint dwAddPower);

		public abstract void SetTarget(uint dwVID, bool bForceChange = true);
		public abstract void NotifyCharacterUpdate(uint dwVID);
		public abstract void NotifyCharacterDead(uint dwVID);
		public abstract void NotifyDeletingCharacterInstance(uint dwVID);
		public abstract void NotifyChangePKMode();

		public abstract void SetObserverMode(bool isEnable);
		public abstract void SetComboSkillFlag(bool bFlag);

		public abstract void StartEmotionProcess();
		public abstract void EndEmotionProcess();

		public abstract CInstanceBase NEW_GetMainActorPtr();
}

