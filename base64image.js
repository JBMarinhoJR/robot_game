// Imagem em formato base64
var base64Image = "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACWSURBVChTdZDLDcQgDERzpwjEJya0QSH0wJFuqIL2vDteGRGkPQy2x08j5IsScQiBiYifJ7Exhr33HGMUzznHlBJfMHLOsgA0xpCKOcTA901srf2BJ7TDKgFhQr13qbXW5S0Qgyac0J4s4JyTW2uyKKVID8F/gTBR//UC4tEFEpGif1VogSosFNp93PUFQieUvscmIv4Afnyd90kNfI8AAAAASUVORK5CYII=";

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