const textSpacyForm = document.querySelector('.text-spacy-form');

const translateText = async (text) => {
    const inferResponse = await fetch(`score_text?text_input=${text}`);
    const inferJson = await inferResponse.json();
    var jsonStr = JSON.stringify(inferJson);
    return jsonStr;
};

textSpacyForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const textSpacyInput = document.getElementById('text-spacy-input');
  const textSpacyParagraph = document.querySelector('.text-spacy-output');

  try {
    textSpacyParagraph.textContent = await translateText(textSpacyInput.value);
  } catch (err) {
    console.error(err);
  }
});