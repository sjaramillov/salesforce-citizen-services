import { LightningElement } from 'lwc';

const DEMO_CASE = {
  citizen: 'Persona Demo A',
  reference: 'CIT-****-4219',
  caseNumber: 'BEN-2026-004219',
  benefit: 'Renovación de beneficio',
  status: 'Documento pendiente',
  missingDocument: 'Comprobante de residencia',
  deadline: '2026-07-05',
  preferredChannel: 'WhatsApp',
  nextAction: 'Cargar documento y confirmar dirección',
  proactiveNotice: 'Recordatorio antes del vencimiento',
  progressLabel: 'Paso 2 de 5',
  sla: '3 días para completar',
  updated: 'Escenario de demostración'
};

const SERVICE_SIGNALS = [
  {
    label: 'Caso en seguimiento',
    value: 'BEN-2026-004219',
    className: 'signal signal--case'
  },
  {
    label: 'Aviso proactivo',
    value: 'Recordatorio ilustrativo',
    className: 'signal signal--channel'
  },
  {
    label: 'Atención humana',
    value: 'Derivación ilustrativa',
    className: 'signal signal--trust'
  }
];

const DOCUMENT_ITEMS = [
  {
    index: '01',
    label: 'Identidad de ejemplo',
    description: 'Datos ficticios; no verifica una identidad real.',
    className: 'document-item document-item--done'
  },
  {
    index: '02',
    label: 'Comprobante pendiente',
    description: 'Falta residencia antes de la fecha límite.',
    className: 'document-item document-item--active'
  },
  {
    index: '03',
    label: 'Revisión posterior',
    description: 'Funcionario valida excepciones si aplica.',
    className: 'document-item'
  }
];

const AGENT_MESSAGES = [
  {
    speaker: 'Ciudadana',
    text: '¿Qué pasa con mi beneficio?',
    className: 'message message--user'
  },
  {
    speaker: 'Asistente CSC',
    text: 'Tu caso está pendiente por comprobante de residencia. Puedo guiarte y avisar a un funcionario si hay una excepción.',
    className: 'message message--agent'
  }
];

const JOURNEY_STEPS = [
  {
    index: '01',
    label: 'Identidad',
    description: 'Validación del caso y referencia ciudadana.',
    className: 'step step--complete'
  },
  {
    index: '02',
    label: 'Documentos',
    description: 'Detección del comprobante pendiente.',
    className: 'step step--active'
  },
  {
    index: '03',
    label: 'Revisión',
    description: 'Funcionario valida excepciones y completitud.',
    className: 'step'
  },
  {
    index: '04',
    label: 'Resolución',
    description: 'Actualización del beneficio y cierre del caso.',
    className: 'step'
  },
  {
    index: '05',
    label: 'Notificación',
    description: 'Respuesta por el canal preferido del ciudadano.',
    className: 'step'
  }
];

const CHANNELS = [
  {
    icon: 'WA',
    name: 'WhatsApp',
    description: 'Consulta rápida para estado, documentos y recordatorios.'
  },
  {
    icon: 'WEB',
    name: 'Portal web',
    description: 'Autoservicio con trazabilidad y carga de soportes.'
  },
  {
    icon: 'TEL',
    name: 'Teléfono',
    description: 'Atención asistida con contexto del caso y resumen previo.'
  },
  {
    icon: 'PTO',
    name: 'Punto presencial',
    description: 'Acompañamiento para ciudadanos con baja adopción digital.'
  }
];

const FAQS = [
  {
    question: '¿Qué documento falta para continuar?',
    answer:
      'Falta el comprobante de residencia. El portal muestra la fecha límite, el canal recomendado y el próximo paso.'
  },
  {
    question: '¿El asistente toma decisiones definitivas?',
    answer:
      'No. El asistente resuelve consultas repetitivas y pasa excepciones a un funcionario con contexto y seguimiento.'
  },
  {
    question: '¿Cómo ayuda el aviso preventivo?',
    answer:
      'Permite recordar vencimientos, renovaciones y documentos pendientes antes de que el ciudadano tenga que reclamar.'
  }
];

export default class CscBenefitPortal extends LightningElement {
  selectedCase = DEMO_CASE;
  serviceSignals = SERVICE_SIGNALS;
  documentItems = DOCUMENT_ITEMS;
  agentMessages = AGENT_MESSAGES;
  journeySteps = JOURNEY_STEPS;
  channels = CHANNELS;
  faqs = FAQS;

  lookupValue = DEMO_CASE.caseNumber;
  lookupMessage = 'Caso ficticio cargado; consulta local sin backend.';
  lookupState = 'info';

  get lookupMessageClass() {
    return `lookup-message lookup-message--${this.lookupState}`;
  }

  handleLookupInput(event) {
    this.lookupValue = event.target.value;
    this.lookupMessage = '';
    this.lookupState = 'info';
  }

  handleLookup() {
    const normalizedValue = (this.lookupValue || '').trim().toUpperCase();

    if (normalizedValue === DEMO_CASE.caseNumber) {
      this.lookupMessage =
        'Caso encontrado. El beneficio está pendiente por comprobante de residencia.';
      this.lookupState = 'success';
      return;
    }

    this.lookupMessage =
      'No encontramos ese caso de referencia. Usa BEN-2026-004219 para mostrar el flujo.';
    this.lookupState = 'warning';
  }

  handleConsult() {
    this.lookupValue = DEMO_CASE.caseNumber;
    this.handleLookup();
  }

  handleAgent() {
    this.lookupMessage =
      'Respuesta de ejemplo: documento pendiente. La derivación humana todavía requiere integración.';
    this.lookupState = 'info';
  }
}
