/**
 * ════════════════════════════════════════════════════════════
 *  Budget Pro — Google Apps Script Sync Server
 *  Auteur : Yaakov · généré avec Claude Code
 * ════════════════════════════════════════════════════════════
 *
 *  INSTALLATION (5 minutes, une seule fois) :
 *  ──────────────────────────────────────────
 *  1. Ouvre Google Sheets → crée un nouveau classeur
 *     Nomme-le "Budget Pro Sync"
 *
 *  2. Dans le menu : Extensions → Apps Script
 *
 *  3. Supprime le contenu par défaut et colle tout ce fichier
 *
 *  4. Clique sur "Enregistrer" (icône disquette)
 *
 *  5. Clique sur "Déployer" → "Nouveau déploiement"
 *     · Type : Application Web
 *     · Exécuter en tant que : Moi
 *     · Accès autorisé à : Tout le monde
 *     → Cliquer "Déployer" → copier l'URL affichée
 *
 *  6. Dans Budget Pro (index.html) :
 *     → Section "ייבוא מנטלי" → coller l'URL → "שמור"
 *
 *  7. Dans le journal de Natalie (natalie-daily-log.html) :
 *     → ⚙️ en haut à gauche → coller la même URL → "שמור"
 *
 *  C'est tout ! Les entrées de Natalie arriveront
 *  automatiquement dans ton Budget Pro.
 * ════════════════════════════════════════════════════════════
 */

// Nom de la feuille dans Google Sheets
const SHEET_NAME = 'Transactions';

// ── Colonnes ────────────────────────────────────────────────
const COLUMNS = ['id', 'date', 'time', 'scope', 'type', 'category', 'amount', 'note'];

/**
 * GET  → Budget Pro demande toutes les transactions
 *        URL : <script_url>?action=get
 */
function doGet(e) {
  const action = e && e.parameter && e.parameter.action;

  if (action === 'get' || !action) {
    const sheet = getOrCreateSheet();
    const rows  = sheet.getDataRange().getValues();

    if (rows.length <= 1) {
      // Feuille vide ou seulement l'en-tête
      return jsonResponse([]);
    }

    const headers = rows[0];
    const data = rows.slice(1).map(row => {
      const obj = {};
      headers.forEach((h, i) => { obj[h] = row[i]; });
      return obj;
    });

    return jsonResponse(data);
  }

  return jsonResponse({ error: 'action inconnue' });
}

/**
 * POST → Natalie envoie une nouvelle transaction
 *        Body : JSON { id, date, time, scope, type, category, amount, note }
 */
function doPost(e) {
  try {
    const entry  = JSON.parse(e.postData.contents);
    const sheet  = getOrCreateSheet();

    // Vérifie si l'ID existe déjà (évite les doublons)
    const existingIds = sheet.getDataRange().getValues().slice(1).map(r => r[0]);
    if (existingIds.includes(entry.id)) {
      return jsonResponse({ status: 'duplicate', id: entry.id });
    }

    // Ajoute la ligne
    sheet.appendRow(COLUMNS.map(col => entry[col] || ''));

    return jsonResponse({ status: 'ok', id: entry.id });

  } catch (err) {
    return jsonResponse({ status: 'error', message: err.message });
  }
}

// ── Helpers ──────────────────────────────────────────────────

function getOrCreateSheet() {
  const ss    = SpreadsheetApp.getActiveSpreadsheet();
  let sheet   = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    // Crée l'en-tête
    sheet.appendRow(COLUMNS);
    sheet.getRange(1, 1, 1, COLUMNS.length)
      .setFontWeight('bold')
      .setBackground('#1B3A5C')
      .setFontColor('#FFFFFF');
    sheet.setFrozenRows(1);
    // Largeur des colonnes
    sheet.setColumnWidth(1, 200); // id
    sheet.setColumnWidth(4, 80);  // scope
    sheet.setColumnWidth(5, 80);  // type
    sheet.setColumnWidth(6, 180); // category
    sheet.setColumnWidth(7, 80);  // amount
  }

  return sheet;
}

function jsonResponse(data) {
  const output = ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
  return output;
}
