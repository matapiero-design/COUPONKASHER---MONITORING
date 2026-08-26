# Nettoyage des emails — run 2026-08-26 (mode : blanc)

Run **a blanc** : rien n'a ete archive ni supprime. Ce rapport dit ce qui *serait* fait.

## Ce qui serait traite

| Regle | Etage | Volume dans la boite | Threads releves |
|---|---|---|---|
| Marketing voyage (compagnies, OTA, hôtels) | corbeille | > 200 | 7 |
| Marketing voyage (compagnies, OTA, hôtels) | archive | > 200 | 5 |
| Marketing grand public (télécom, retail, petites annonces) | archive | > 200 | 5 |
| Notifications produit et onboarding SaaS | archive | > 200 | 5 |
| Divrei Torah et listes de Tehilim | archive | > 200 | 2 |
| Marketing grand public (télécom, retail, petites annonces) | corbeille | > 200 | 1 |
| Notifications produit et onboarding SaaS | corbeille | > 200 | 1 |
| Veille concurrence — offres casher | archive | 1 | 1 |
| **Total** | | | **27** |

> Les volumes marques `>` sont plafonnes par l'API Gmail, qui cesse de compter au-dela de 200 threads. Le vrai volume est superieur, parfois de beaucoup.

## Par expediteur

| Expediteur | Threads |
|---|---|
| marketing@ma.elal-mail.com | 7 |
| no-reply@mail.yad2.co.il | 3 |
| kayak@msg.kayak.com | 2 |
| elal@ma.elalmatmid.com | 2 |
| google-noreply@google.com | 2 |
| connect@cdata.com | 2 |
| travel@kiwi.com | 1 |
| tickchak@tickmail.co.il | 1 |
| sarah@2236142.brevosend.com | 1 |
| interspace@intervision.co.il | 1 |
| noreply@traveler.md | 1 |
| analytics-noreply@google.com | 1 |
| beismedrash@themir.org.il | 1 |
| mail@tehilimyahad.com | 1 |
| leah@gokosher.com | 1 |

## Ecartes par les protections

Ces threads matchaient une regle mais ont ete retenus. **Ils restent en place.**

| Expediteur | Sujet | Motif |
|---|---|---|
| elal@ma.elalmatmid.com | מוריס, מצטרפים ומקבלים כרטיס טיסה מתנה! פרסומת | mot-cle sujet : כרטיס טיסה |
| elal@ma.elalmatmid.com | מוריס, כרטיס טיסה עליכם, ראש שקט עלינו! פרסומת | mot-cle sujet : כרטיס טיסה |
| marketing@ma.elal-mail.com | מזמינים היום כרטיס טיסה למגוון יעדים ומקבל 10,000 נקודות מתנה! | mot-cle sujet : כרטיס טיסה |
| marketing@ma.elal-mail.com | עדכון מדיניות ההזמנות באל על - Booking Policy | mot-cle sujet : booking |
| contact@alloj.com | TENTEZ DE REMPORTER UNE ROLEX ! Jouez et prenez votre ticket | mot-cle sujet : ticket |

---

_Genere par `pipeline/email_cleanup.py` le 2026-08-26 12:41 UTC._
