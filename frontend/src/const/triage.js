export const TRIAGE_LEVELS = {
    'emergency_ambulance': { label: 'Call an ambulance immediately', color: 'bg-red-100 text-red-800 border-red-300', icon: 'pi-phone' },
    'emergency': { label: 'Go to the nearest emergency department', color: 'bg-orange-100 text-orange-800 border-orange-300', icon: 'pi-exclamation-triangle' },
    'consultation_24': { label: 'Consult a doctor within 24 hours', color: 'bg-yellow-100 text-yellow-800 border-yellow-300', icon: 'pi-clock' },
    'consultation': { label: 'Consult a doctor', color: 'bg-blue-100 text-blue-800 border-blue-300', icon: 'pi-calendar' },
    'self_care': { label: 'Self care at home', color: 'bg-green-100 text-green-800 border-green-300', icon: 'pi-home' }
  }