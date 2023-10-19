// Imagem em formato base64



var base64Image = "iVBORw0KGgoAAAANSUhEUgAAAGYAAAAJCAIAAABPH866AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABWSURBVEhLY1BQUh1FJCFQkOnrThxFRCJokJkZLx9FRCJokDk7HBhFRCJokAUH3BpFRCJokKUmfRhFRCJokJUU/h9FRCJokDXU/h9FRCJokI0iEpCSKgACWWDDFfY5XwAAAABJRU5ErkJggg==";

// Crie um Blob a partir da string base64
var byteCharacters = atob(base64Image);
var byteNumbers = new Array(byteCharacters.length);
for (var i = 0; i < byteCharacters.length; i++) {
    byteNumbers[i] = byteCharacters.charCodeAt(i);
}
var byteArray = new Uint8Array(byteNumbers);
var blob = new Blob([byteArray], { type: 'image/png' });

// Crie uma URL de objeto para o Blob
var blobUrl = URL.createObjectURL(blob);

// Abra a URL em uma nova aba
window.open(blobUrl);