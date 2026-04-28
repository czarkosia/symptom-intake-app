const baseUrl = import.meta.env.VITE_BACKEND_URI;

/**
 * @typedef {Object} Choice
 * @property {string} id
 * @property {string} label
 */

/**
 * @typedef {Object} QuestionResponse
 * @property {string} question_text
 * @property {string} item_id
 * @property {string} name
 * @property {Choice[]} choices
 */

/**
 * @typedef {Object} Condition
 * @property {string} id
 * @property {string} name
 * @property {number} probability
 */

/**
 * @typedef {Object} FinalResponse
 * @property {string} triage_level
 * @property {Condition[]} conditions
 */

/**
 * @typedef {Object} EvidenceSummaryItem
 * @property {string} item_id
 * @property {string} choice_id
 */

/**
 * @typedef {Object} ResultResponse
 * @property {string} interview_id
 * @property {boolean} is_finished
 * @property {FinalResponse} [final_response]
 * @property {QuestionResponse} [question_response]
 * @property {EvidenceSummaryItem[]} evidence_summary
 */

/**
 * @param {Object} formData
 * @returns {Promise<ResultResponse>}
 */
export const startInterviewCall = async (formData) => {
  const response = await fetch(`${baseUrl}/api/v1/interview/start`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Internal server error.');
  }

  return await response.json();
}

/**
 * @param {Object} answerData
 * @returns {Promise<ResultResponse>}
 */
export const answerQuestionCall = async (answerData) => {
  const response = await fetch(`${baseUrl}/api/v1/interview/answer`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(answerData)
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Internal server error.');
  }

  return await response.json();
}